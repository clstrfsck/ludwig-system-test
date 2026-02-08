from systest import simple_edit_test, syntax_error

# LEADING PARAMETER: [none, + , - ,    ,    , > , < ,   ] EQC

def test_no_leading_parameter_success():
    simple_edit_test("eqc/1/[i/yes/:i/no/]", "abc\n", "yesabc\n")

def test_no_leading_parameter_fail():
    simple_edit_test("jeqc/1/[i/yes/:i/no/]", "abc\n", "anobc\n")

def test_plus_leading_parameter_success():
    simple_edit_test("+eqc/1/[i/yes/:i/no/]", "abc\n", "yesabc\n")

def test_minus_leading_parameter_success():
    simple_edit_test("j-eqc/1/[i/yes/:i/no/]", "abc\n", "ayesbc\n")

def test_minus_leading_parameter_fail():
    simple_edit_test("j-eqc/2/[i/yes/:i/no/]", "abc\n", "anobc\n")

def test_gt_leading_parameter_before_column():
    simple_edit_test(">eqc/2/[i/yes/:i/no/]", "abc\n", "noabc\n")

def test_gt_leading_parameter_at_column():
    simple_edit_test("j>eqc/2/[i/yes/:i/no/]", "abc\n", "ayesbc\n")

def test_gt_leading_parameter_after_column():
    simple_edit_test("2j>eqc/2/[i/yes/:i/no/]", "abc\n", "abyesc\n")

def test_lt_leading_parameter_before_column():
    simple_edit_test("<eqc/2/[i/yes/:i/no/]", "abc\n", "yesabc\n")

def test_lt_leading_parameter_at_column():
    simple_edit_test("j<eqc/2/[i/yes/:i/no/]", "abc\n", "ayesbc\n")

def test_lt_leading_parameter_after_column():
    simple_edit_test("2j<eqc/2/[i/yes/:i/no/]", "abc\n", "abnoc\n")
