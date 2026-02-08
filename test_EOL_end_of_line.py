from systest import simple_edit_test, syntax_error

# LEADING PARAMETER: [none, + , - ,    ,    , > , < ,   ] EOL

def test_no_leading_parameter_success():
    simple_edit_test(">jeol[i/yes/:i/no/]", "abc\n", "abcyes\n")

def test_no_leading_parameter_fail():
    simple_edit_test("eol[i/yes/:i/no/]", "abc\n", "noabc\n")

def test_plus_leading_parameter_success():
    simple_edit_test(">j+eol[i/yes/:i/no/]", "abc\n", "abcyes\n")

def test_minus_leading_parameter_success():
    simple_edit_test("-eol[i/yes/:i/no/]", "abc\n", "yesabc\n")

def test_minus_leading_parameter_fail():
    simple_edit_test(">j-eol[i/yes/:i/no/]", "abc\n", "abcno\n")

def test_gt_leading_parameter_before_end():
    simple_edit_test(">j-j>eol[i/yes/:i/no/]", "abc\n", "abnoc\n")

def test_gt_leading_parameter_at_end():
    simple_edit_test(">j>eol[i/yes/:i/no/]", "abc\n", "abcyes\n")

def test_gt_leading_parameter_after_end():
    simple_edit_test(">jzr>eol[i/yes/:i/no/]", "abc\n", "abc yes\n")

def test_lt_leading_parameter_before_end():
    simple_edit_test(">j-j<eol[i/yes/:i/no/]", "abc\n", "abyesc\n")

def test_lt_leading_parameter_at_end():
    simple_edit_test(">j<eol[i/yes/:i/no/]", "abc\n", "abcyes\n")

def test_lt_leading_parameter_after_end():
    simple_edit_test(">jzr<eol[i/yes/:i/no/]", "abc\n", "abc no\n")
