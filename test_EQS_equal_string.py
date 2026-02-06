from systest import simple_edit_test, syntax_error

#  LEADING PARAMETER: [none, + , - ,    ,    , > , < ,   ] EQS

def test_no_leading_parameter():
    simple_edit_test("eqs/abc/[i/yes/:i/no/]", "ABCabc\n", "yesABCabc\n")

def test_no_leading_parameter_exact():
    simple_edit_test("eqs\"ABC\"[i/yes/:i/no/]", "ABCabc\n", "yesABCabc\n")

def test_no_leading_parameter_fail():
    simple_edit_test("eqs\"XYZ\"[i/yes/:i/no/]", "ABCabc\n", "noABCabc\n")

def test_plus_leading_parameter():
    simple_edit_test("+eqs/abc/[i/yes/:i/no/]", "ABCabc\n", "yesABCabc\n")

def test_minus_leading_parameter():
    simple_edit_test("-eqs/abc/[i/yes/:i/no/]", "ABCabc\n", "noABCabc\n")

def test_gt_leading_parameter():
    simple_edit_test(">eqs/abc/[i/yes/:i/no/]", "abc\n", "yesabc\n")

def test_gt_leading_parameter_fail():
    simple_edit_test(">eqs/xyz/[i/yes/:i/no/]", "abc\n", "noabc\n")

def test_lt_leading_parameter():
    simple_edit_test("<eqs/abc/[i/yes/:i/no/]", "abc\n", "yesabc\n")

def test_lt_leading_parameter_fail():
    simple_edit_test("<eqs/abc/[i/yes/:i/no/]", "xyz\n", "noxyz\n")
