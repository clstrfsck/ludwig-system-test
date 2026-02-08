from systest import simple_edit_test

# LEADING PARAMETER: [none,   ,   ,    ,    ,   ,   ,   ] SA

def test_no_leading_parameter():
    simple_edit_test("sa/t/abc/sc/t/", "def\n", "abcdef\n")

def test_no_leading_parameter_deref():
    simple_edit_test("sa/t1/abc/sa/t2/$t1$/sc/t2/", "def\n", "abcdef\n")