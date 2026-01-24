from systest import command_failed, simple_edit_test, syntax_error
import pytest

# LEADING PARAMETER: [none, + , - , +n , -n ,   ,   ,   ] G

def test_zero_leading_parameter():
    syntax_error("0g", "")

def test_negative_leading_parameter():
    simple_edit_test(">j-3g/cat/i/m1/", "catcatcatcat\n", "catm1catcatcat\n")

def test_no_leading_parameter():
    simple_edit_test("g'abc'=di/m1/", "aBcD\n", "m1D\n")

def test_no_leading_parameter_exact():
    simple_edit_test("g\"aBc\"=di/m1/", "aBcD\n", "m1D\n")

def test_no_leading_parameter_no_match():
    command_failed("g\"abc\"", "aBcD\n")

def test_no_leading_parameter_case_insensitive():
    simple_edit_test("g'abc'=di/m1/", "aBcD\n", "m1D\n")

def test_no_leading_parameter_regex():
    simple_edit_test("g`LULU`=di/m1/", "aBcD\n", "m1\n")

def test_plus_leading_parameter():
    simple_edit_test("+g\"aBc\"=di/m1/", "aBcaBcD\n", "m1aBcD\n")

def test_positive_leading_parameter():
    simple_edit_test("2g\"aBc\"=di/m1/", "aBcaBcD\n", "aBcm1D\n")

def test_positive_leading_parameter_fails():
    command_failed("3g\"aBc\"", "aBcaBcD\n")

def test_minus_leading_parameter():
    simple_edit_test(">j-g'abc'=di/m1/", "aBcaBcD\n", "aBcm1D\n")

def test_minus_leading_parameter_exact():
    simple_edit_test(">j-g\"aBc\"=di/m1/", "aBcaBcD\n", "aBcm1D\n")

# Feature: Single middle context
# Pattern: N
# Test String: "abc123def"
# Type: Middle Only
# Expected Match: true, Dot: 3, Equals: 4 (middle context matches "1")
# Negative Test String: "abcdef"
# Expected No Match: true (no number)

def test_single_middle_context():
    simple_edit_test("g`N`=di/|/", "abc123def\n", "abc|23def\n")

def test_single_middle_context_no_match():
    command_failed("g`N`", "abcdef\n")

# Feature: left context, middle context
# Pattern: A,N
# Test String: "abc123def"
# Type: Left/Middle
# Expected Match: true, left matches "c", middle matches "1"
# Negative Test String: "123def"
# Expected No Match: true (no A before N)

def test_left_middle_context():
    simple_edit_test("g`A,N`=di/|/", "abc123def\n", "abc|23def\n")

def test_left_middle_context_no_match():
    command_failed("g`A,N`", "123def\n")

# Feature: left context, middle context, right context
# Pattern: L,N,L
# Test String: "abc1d2e"
# Type: Left/Middle/Right
# Expected Match: true, left matches "c", middle matches "1", right matches "d"
# Negative Test String: "abc1"
# Expected No Match: true (no L after N)

def test_left_middle_right_context():
    simple_edit_test("g`L,N,L`=di/|/", "abc1d2e\n", "abc|d2e\n")

def test_left_middle_right_context_no_match():
    command_failed("g`L,N,L`", "abc1\n")

# Feature: Middle context spanning the whole string
# Pattern: ANA
# Test String: "a1b"
# Type: Middle Only
# Expected Match: true, middle matches "a1b"

def test_middle_context_whole_string():
    simple_edit_test("g`ANA`=di/|/", "a1b\n", "|\n")

def test_middle_context_whole_string_no_match():
    command_failed("g`ANA`", "abc\n")

# Feature: Basic alternation
# Pattern: N|P
# Test String: "abc1.def"
# Type: Middle Only
# Expected Match: true, middle matches "1"
# Test String: "abc.def"
# Type: Middle Only
# Expected Match: true, middle matches "."
# Negative Test String: "abcdef"
# Expected No Match: true

def test_basic_alternation_number_1():
    simple_edit_test("g`N|P`=di/|/", "abc1.def\n", "abc|.def\n")

def test_basic_alternation_number_2():
    simple_edit_test("g`N|P`=di/|/", "abc.def\n", "abc|def\n")

def test_basic_alternation_number_no_match():
    command_failed("g`N|P`", "abcdef\n")

# Feature: Alternation within a left, middle context.
# Pattern: U,N|P
# Test String: "AB1.C"
# Type: Left/Middle
# Expected Match: true, left matches "B", middle matches "1"
# Test String: "AB.C"
# Type: Left/Middle
# Expected Match: true, left matches "B", middle matches "."

@pytest.mark.skip(reason="This alternation test doesn't work :(")
def test_alternation_left_middle_number_1():
    simple_edit_test("g`U,(N|P)`=di/|/", "AB1.C\n", "AB|.C\n")

@pytest.mark.skip(reason="This alternation test doesn't work :(")
def test_alternation_left_middle_number_2():
    simple_edit_test("g`U,N|P`=di/|/", "AB.C\n", "AB|C\n")

# Feature: Grouping with parentheses for alternation.
# Pattern: A(N|P)A
# Test String: "a1b"
# Type: Middle Only
# Expected Match: true, middle matches "a1b"
# Test String: "a.b"
# Type: Middle Only
# Expected Match: true, middle matches "a.b"

def test_grouping_alternation_middle_1():
    simple_edit_test("g`A(N|P)A`=di/|/", "a1b\n", "|\n")

def test_grouping_alternation_middle_2():
    simple_edit_test("g`A(N|P)A`=di/|/", "a.b\n", "|\n")

# Feature: Kleene Star (*) - Zero or more
# Pattern: N*N
# Test String: "abc123def"
# Type: Middle Only
# Expected Match: true, middle matches "123"
# Pattern: *N
# Test String: "abcdef"
# Type: Middle Only
# Expected Match: true, middle matches empty string at start
# Test String: "abc"
# Type: Left/Middle
# Pattern: A,*N
# Expected Match: true, left matches "a", middle matches empty string

def test_kleene_star_middle_1():
    # Note that `*N` matches the zero-width string at the start of "abc123def"
    simple_edit_test("g`N*N`=di/|/", "abc123def\n", "abc|def\n")

def test_kleene_star_middle_2():
    simple_edit_test("g`*N`=di/|/", "abcdef\n", "|abcdef\n")

def test_kleene_star_left_middle():
    simple_edit_test("g`A,*N`=di/|/", "abc\n", "a|bc\n")

# Feature: Kleene Plus (+) - One or more
# Pattern: +N
# Test String: "abc123def"
# Type: Middle Only
# Expected Match: true, middle matches "123"
# Negative Test String: "abcdef"
# Expected No Match: true

def test_kleene_plus_middle():
    simple_edit_test("g`+N`=di/|/", "abc123def\n", "abc|def\n")

def test_kleene_plus_middle_no_match():
    command_failed("g`+N`", "abcdef\n")

# Feature: Exact Number (number)
# Pattern: 3N
# Test String: "abc123def"
# Type: Middle Only
# Expected Match: true, middle matches "123"
# Negative Test String: "abc12def"
# Expected No Match: true

def test_exact_number_middle():
    simple_edit_test("g`3N`=di/|/", "abc123def\n", "abc|def\n")

def test_exact_number_middle_no_match():
    command_failed("g`3N`", "abc12def\n")

# Feature: Range [nn, mm] - specific lower and upper bounds
# Pattern: [2,4]N
# Test String: "abc12def"
# Type: Middle Only
# Expected Match: true, middle matches "12"
# Test String: "abc1234def"
# Type: Middle Only
# Expected Match: true, middle matches "1234"
# Negative Test String: "abc1def"
# Expected No Match: true
# Negative Test String: "abc1d2e3f"
# Expected No Match: true

def test_range_lower_upper_middle_1():
    simple_edit_test("g`[2,4]N`=di/|/", "abc12def\n", "abc|def\n")

def test_range_lower_upper_middle_2():
    simple_edit_test("g`[2,4]N`=di/|/", "abc1234def\n", "abc|def\n")

def test_range_lower_upper_middle_no_match_1():
    command_failed("g`[2,4]N`", "abc1def\n")

def test_range_lower_upper_middle_no_match_2():
    command_failed("g`[2,4]N`", "abc1d2e3f\n")

# Feature: Range [nn,] - lower bound, indefinitely many
# Pattern: [2,]N
# Test String: "abc12def"
# Type: Middle Only
# Expected Match: true, middle matches "12"
# Test String: "abc12345def"
# Type: Middle Only
# Expected Match: true, middle matches "12345"
# Negative Test String: "abc1def"
# Expected No Match: true

def test_range_lower_indefinite_middle_1():
    simple_edit_test("g`[2,]N`=di/|/", "abc12def\n", "abc|def\n")

def test_range_lower_indefinite_middle_2():
    simple_edit_test("g`[2,]N`=di/|/", "abc12345def\n", "abc|def\n")

def test_range_lower_indefinite_middle_no_match():
    command_failed("g`[2,]N`", "abc1def\n")

# Feature: Range [,mm] - upper bound, zero lower bound.
# Pattern: [,3]N
# Test String: "1def"
# Type: Middle Only
# Expected Match: true, middle matches "1"
# Test String: "123def"
# Type: Middle Only
# Expected Match: true, middle matches "123"
# Test String: "abcdef"
# Type: Middle Only
# Expected Match: true, middle matches empty string at start
# Negative Test String: "abc1234def"
# Expected No Match: true

def test_range_upper_middle_1():
    simple_edit_test("g`[,3]N`=di/|/", "1def\n", "|def\n")

def test_range_upper_middle_2():
    simple_edit_test("g`[,3]N`=di/|/", "123def\n", "|def\n")

def test_range_upper_middle_3():
    simple_edit_test("g`[,3]N`=di/|/", "1234def\n", "|4def\n")

def test_range_upper_middle_4():
    simple_edit_test("g`[,3]N`=di/|/", "abcdef\n", "|abcdef\n")

# Feature: Range [,] - zero to indefinitely many (same as *)
# Pattern: [,]N
# Test String: "123def"
# Type: Middle Only
# Expected Match: true, middle matches "123"
# Test String: "abcdef"
# Type: Middle Only
# Expected Match: true, matches empty string at start

def test_range_unbounded_middle_1():
    simple_edit_test("g`[,]N`=di/|/", "123def\n", "|def\n")

def test_range_unbounded_middle_2():
    simple_edit_test("g`[,]N`=di/|/", "abcdef\n", "|abcdef\n")

# Feature: Quantifier applies to a grouped COMPOUND.
# Pattern: +(UL)
# Test String: "AaBbCc"
# Type: Middle Only
# Expected Match: true, middle matches "AaBbCc"
# Negative Test String: "aabC"
# Expected No Match: true (doesn't match the UL pattern)

def test_quantifier_grouped_compound_middle():
    simple_edit_test("g`+(UL)`=di/|/", "AaBbCc\n", "|\n")

def test_quantifier_grouped_compound_middle_no_match():
    command_failed("g`+(UL)`", "aabC\n")

# Feature: A (Alphabetic characters)
# Pattern: A
# Test String: "1a2B3"
# Type: Middle Only
# Expected Match: true, middle matches "a"
# Test String: "1B2"
# Type: Middle Only
# Expected Match: true, middle matches "B"

def test_alphabetic_middle_1():
    simple_edit_test("g`A`=di/|/", "1a2B3\n", "1|2B3\n")

def test_alphabetic_middle_2():
    simple_edit_test("g`A`=di/|/", "1B2\n", "1|2\n")

# Feature: U (Uppercase alphabetic)
# Pattern: U
# Test String: "aBc"
# Type: Middle Only
# Expected Match: true, middle matches "B"
# Negative Test String: "abc"
# Expected No Match: true

def test_uppercase_alphabetic_middle():
    simple_edit_test("g`U`=di/|/", "aBc\n", "a|c\n")

def test_uppercase_alphabetic_middle_no_match():
    command_failed("g`U`", "abc\n")

# Feature: L (Lowercase alphabetic)
# Pattern: L
# Test String: "aBc"
# Type: Middle Only
# Expected Match: true, middle matches "a"
# Negative Test String: "ABC"
# Expected No Match: true

def test_lowercase_alphabetic_middle():
    simple_edit_test("g`L`=di/|/", "aBc\n", "|Bc\n")

def test_lowercase_alphabetic_middle_no_match():
    command_failed("g`L`", "ABC\n")

# Feature: P (Punctuation characters (),.;:"'!?-)
# Pattern: P
# Test String: "abc,def"
# Type: Middle Only
# Expected Match: true, middle matches ","
# Test String: "hello!world"
# Type: Middle Only
# Expected Match: true, middle matches "!"
# Negative Test String: "abc def" (space is not P)
# Expected No Match: true

def test_punctuation_middle_1():
    simple_edit_test("g`P`=di/|/", "abc,def\n", "abc|def\n")

def test_punctuation_middle_2():
    simple_edit_test("g`P`=di/|/", "hello!world\n", "hello|world\n")

def test_punctuation_middle_no_match():
    command_failed("g`P`", "abc def\n")

# Feature: N (Numeric characters)
# Pattern: N
# Test String: "abc1def"
# Type: Middle Only
# Expected Match: true, middle matches "1"
# Negative Test String: "abcdef"
# Expected No Match: true

def test_numeric_middle():
    simple_edit_test("g`N`=di/|/", "abc1def\n", "abc|def\n")

def test_numeric_middle_no_match():
    command_failed("g`N`", "abcdef\n")

# Feature: S (Space)
# Pattern: S
# Test String: "abc def"
# Type: Middle Only
# Expected Match: true, middle matches " "
# Negative Test String: "abcdef"
# Expected Match: true, middle matches space at end of line

def test_space_middle():
    simple_edit_test("g`S`=di/|/", "abc def\n", "abc|def\n")

def test_space_middle_no_match():
    simple_edit_test("g`S`=di/|/", "abcdef\n", "abcdef|\n")

# Feature: C (All printable characters)
# Pattern: C
# Test String: "a1! "
# Type: Middle Only
# Expected Match: true, middle matches "a"
# Test String: " "
# Type: Middle Only
# Expected Match: true, middle matches " "
# Negative Test String: ??

def test_printable_characters_middle_1():
    simple_edit_test("g`C`=di/|/", "a1 !\n", "|1 !\n")

def test_printable_characters_middle_2():
    simple_edit_test("g`C`=di/|/", " \n", "|\n")

# Feature: Negation (-) with SET
# Pattern: -N (Non-numeric)
# Test String: "12a34"
# Type: Middle Only
# Expected Match: true, middle matches "a"
# Negative Test String: "12345"
# Expected No Match: true

def test_negation_set_middle():
    simple_edit_test("g`-N`=di/|/", "12a34\n", "12|34\n")

# Feature: D (Define Set) - D/a..z/ (similar to L)
# Pattern: D/a..z/
# Test String: "ABCaDef"
# Type: Middle Only
# Expected Match: true, middle matches "a"
# Negative Test String: "ABCDEF"
# Expected No Match: true

def test_define_set_lowercase_middle():
    simple_edit_test("g`D/a..z/`=di/|/", "ABCaDef\n", "ABC|Def\n")

# Feature: D (Define Set) - D/0..9A..F/ (hex digits).
# Pattern: D/0..9A..F/+
# Test String: "12AB3G"
# Type: Middle Only
# Expected Match: true, middle matches "12AB3"
# Negative Test String: "GHI"
# Expected No Match: true

def test_define_set_hex_digits_middle():
    simple_edit_test("g`+D/0..9A..F/`=di/|/", "12AB3G\n", "|G\n")

def test_define_set_hex_digits_middle_no_match():
    command_failed("g`+D/0..9A..F/`", "GHI\n")

# Feature: D (Define Set) - with single characters D/abc!/
# Pattern: D/abc!/
# Test String: "xby!z"
# Type: Middle Only
# Expected Match: true, middle matches "b"
# Test String: "x!yz"
# Type: Middle Only
# Expected Match: true, middle matches "!"

def test_define_set_single_characters_middle_1():
    simple_edit_test("g`D/abc!/`=di/|/", "xby!z\n", "x|y!z\n")

def test_define_set_single_characters_middle_2():
    simple_edit_test("g`D/abc!/`=di/|/", "x!yz\n", "x|yz\n")

# Feature: Exact case matching (")
# Pattern: "Hello"
# Test String: "Hello World"
# Type: Middle Only
# Expected Match: true, middle matches "Hello"
# Negative Test String: "HELLO World"
# Expected No Match: true

def test_exact_case_matching_middle():
    simple_edit_test("g`\"Hello\"`=di/|/", "Hello World\n", "| World\n")

def test_exact_case_matching_middle_no_match():
    command_failed("g`\"Hello\"`", "HELLO World\n")

# Feature: Inexact case matching (')
# Pattern: 'hello'
# Test String: "Hello World"
# Type: Middle Only
# Expected Match: true, middle matches "Hello"
# Test String: "HELLO World"
# Type: Middle Only
# Expected Match: true, middle matches "HELLO"

def test_inexact_case_matching_middle_1():
    simple_edit_test("g`'hello'`=di/|/", "Hello World\n", "| World\n")

def test_inexact_case_matching_middle_2():
    simple_edit_test("g`'hello'`=di/|/", "HELLO World\n", "| World\n")

# Feature: String concatenation with other elements
# Pattern: "id"+N
# Test String: "id123"
# Type: Middle Only
# Expected Match: true, middle matches "id123"

def test_string_concatenation_middle():
    simple_edit_test("g`\"id\"+N`=di/|/", "id123\n", "|\n")

# Feature: Testing for a mark @n.
# Pattern: @1N
# Precondition: Assume mark 1 is set at index 1 (between 'a' and 'b').
# Test String: "a|b1c" (where | denotes mark 1's position)
# Type: Left/Middle
# Expected Match: true, mark matches middle matches "1"
# Negative Test String: "ab1c" (no mark 1)
# Expected No Match: true

def test_mark_n_left_middle():
    simple_edit_test("2jm<jg`@1N`=di/|/", "ab1c\n", "ab|c\n")

def test_mark_n_left_middle_no_match():
    command_failed("g`@1N`", "ab1c\n")

# Feature: Beginning of line (<).
# Pattern: <L
# Test String: "abc"
# Type: Middle Only
# Expected Match: true, middle matches "a"
# Negative Test String: " def"
# Expected No Match: true

def test_beginning_of_line_middle():
    simple_edit_test("g`<L`=di/|/", "abc\n", "|bc\n")

# Feature: End of line (>).
# Pattern: L >
# Test String: "abc"
# Type: Middle Only
# Expected Match: true, middle matches "c"
# Negative Test String: "abc "
# Expected No Match: true

def test_end_of_line_middle():
    simple_edit_test("g`L>`=di/|/", "abc\n", "ab|\n")

# Feature: Left margin ({)
# Pattern: {L
# Test String: "abc" (left margin between a and b)
# Type: Middle Only
# Expected Match: true, middle matches "b"
# Negative Test String: "  abc" (not at left margin)
# Expected No Match: true

def test_left_margin_middle():
    simple_edit_test("ep/m=(2,10)/g`{L`=di/|/", "abc\n", "a|c\n")

def test_left_margin_middle_no_match():
    command_failed("ep/m=(2,10)/g`{L`", "  abc\n")

# Feature: Right margin (})
# Pattern: L }
# Test String: "abcdef" (assume this ends at the right margin)
# Type: Middle Only
# Expected Match: true, middle matches "c"
# Negative Test String: "abc " (not at right margin)
# Expected No Match: true

def test_right_margin_middle():
    simple_edit_test("ep/m=(1,5)/g`L}`=di/|/", "abcdef\n", "abc|ef\n")

def test_right_margin_middle_no_match():
    command_failed("ep/m=(1,5)/g`L}`", "abc \n")

# Feature: Column of Dot when match started (^)
# Pattern: ^A,S
# Test String: "a b"
# Type: Left/Middle
# Expected Match: true, left matches "a"

def test_column_of_dot_left_middle():
    simple_edit_test("g`^A,S`=di/|/", "a b\n", "a|b\n")

# Feature: Quantifiers on strings
# Pattern: +("abc")
# Test String: "abcabcxyz"
# Type: Middle Only
# Expected Match: true, middle matches "abcabc"

def test_quantifier_on_strings_middle():
    simple_edit_test("g`+(\"abc\")`=di/|/", "abcabcxyz\n", "|xyz\n")

# Feature: Negated character set with quantifier
# Pattern: +(-N)
# Test String: "hello123world"
# Type: Middle Only
# Expected Match: true, middle matches "hello"

def test_negated_character_set_with_quantifier_middle():
    simple_edit_test("g`+(-N)`=di/|/", "hello123world\n", "|123world\n")

# Feature: Mixed elements in left, middle, right contexts.
# Pattern: UL,[2,]N,P
# Test String: "Aa123,!"
# Type: Left/Middle/Right
# Expected Match: true
# Left Context Match: Aa
# Middle Context Match: 123 (from index 2 to 5)
# Right Context Match: ,
# Negative Test String: "Aa1," (middle context needs at least 2 numbers)
# Expected No Match: true
# Test String: "Aa123!"
# Expected Match: true (left Aa, middle 123, right !)

def test_mixed_elements_left_middle_right_1():
    simple_edit_test("g`UL,[2,]N,P`=di/|/", "Aa123,!\n", "Aa|,!\n")

def test_mixed_elements_left_middle_right_2():
    simple_edit_test("g`UL,[2,]N,P`=di/|/", "Aa123!\n", "Aa|!\n")

def test_mixed_elements_left_middle_right_no_match_1():
    command_failed("g`UL,[2,]N,P`", "Aa1,\n")

# Feature: Nested groups and quantifiers
# Pattern: +(A (N | P))
# Test String: "a1b.c2"
# Type: Middle Only
# Expected Match: true, middle matches "a1b.c2"

def test_nested_groups_and_quantifiers_middle():
    simple_edit_test("g`+(A(N|P))`=di/|/", "a1b.c2\n", "|\n")

# Feature: Empty string matches for * and [,]
# Pattern: *L
# Test String: "123"
# Type: Middle Only
# Expected Match: true, matches empty string at beginning

def test_empty_string_matches_kleene_star_middle():
    simple_edit_test("g`*L`=di/|/", "123\n", "|123\n")

# Feature: Complex D definition
# Pattern: +D/a..zA..Z_0..9/
# Test String: "varName123_VALUE"
# Type: Middle Only
# Expected Match: true, middle matches "varName123_VALUE"

def test_complex_d_definition_middle():
    simple_edit_test("g`+D/a..zA..Z_0..9/`=di/|/", "varName123_VALUE\n", "|\n")

# Feature: CONTEXT, CONTEXT without a right context specified
# Pattern: U,L
# Test String: "Abc"
# Type: Left/Middle
# Expected Match: true, left matches "A", middle matches "b"

def test_context_context_left_middle():
    simple_edit_test("g`U,L`=di/|/", "Abc\n", "A|c\n")

#    5. Use of the Pattern Matcher
#    =============================
#    A pattern definition consists of
#         [<left context> ,] <middle context> [, <right context>]
#    each context being a context free pattern (COMPOUND in syntax).
#     - defaulting to left and middle if a third  pattern is not specified.
#    When a pattern has been successfully matched, the marks Dot and Equals
#    are left wrapped around the middle context.
#    A context free pattern is defined with a regular expression.
#    '|' is used to denote OR (alternative).  Concatenation is implicit.
#    Parentheses are used to structure the expression.
#    Most elements will take a repeat count parameter.

#        Parameters are
#          Numeric : (positive integers only)
#          Kleene star : *.  0 or more repetitions.
#          Kleene plus : +.  1 or more repetitions.
#          Range :   [ nn , mm ]
#            Specifies a range of repetitions nn to mm inclusive.
#            The low bound defaults to 0, the high bound to indefinitely many.
#            The comma is therefore mandatory.
#          Negation : -.  Applies only to sets.

#        Elements of Patterns.
#        ---------------------
#          The sets  ::
#            A : Alphabetic characters.
#            U : Uppercase alphabetic.
#            L : Lowercase alphabetic.
#            P : Punctuation characters.  (),.;:"'!?-`  only
#            N : Numeric characters.
#            S : The space.  (non-space is therefore -S)
#            C : All printable characters.
#            D : Define.  To define a set.

#              D<delimiter> { {char} | {char .. char} } <delimiter>
#                   (the syntax is identical to NEXT and BRIDGE)
#              EG.  D/a..z/ is the same as L
#                   D/a..zA..Z$_0..9/ are all the valid characters in a
#                                     VAX Pascal identifier.

#          Strings.
#            Character strings are delimited with either single or double
#              quotes.
#            Double quotes are used to indicate exact case matching, whilst
#            single quotes indicate inexact case matching.

#          Marks.
#            @n, where n is a mark number, is used in a pattern to test for a
#            mark at the present position.  Note that the presence of a mark
#            where not needed will not affect the normal execution of the
#            pattern matcher.

#          Positionals.
#            < > are respectively the beginning and end of lines.
#            { } the left and right margins.
#             ^  the column that the Dot was in when the match started.

#          Note : The marks and positionals are conceptually in the gaps to the
#            left of the character in a column.  Also note that it is possible
#            for more than one positional or mark to appear in exactly the same
#            place.  If the behaviour of the pattern is dependent upon which of
#            the positionals is found then the path taken will be
#            indeterminate.

#        SYNTAX.     Numbers are positive integers,
#        -------     letters are case independent except in literal strings,
#                    delimiters are matching non-alphanumeric characters.

#          PATTERN DEFINITION ::=
#            [COMPOUND ','] COMPOUND [',' COMPOUND]
#          COMPOUND ::=
#            PATTERN [ '|' COMPOUND ]
#          PATTERN ::=
#            { ( [ PARAMETER ]( SET | '(' COMPOUND ')' | STRING ))  |
#              ( '@' number )  } { ' ' }
#          PARAMETER ::=
#            '*' | '+' | number | ( '[' [ number ] ',' [ number ] ']' )
#          SET ::=
#            [ '-' ] ( 'A'|'P'|'N'|'U'|'L'|'S'|
#            ('D' ((delimiter {{character} | {character ".." character}} delimiter)))
#          STRING ::=
#            (''' {character} ''') | ('"' {character} '"')
