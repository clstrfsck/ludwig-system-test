from systest import simple_edit_test

# LEADING PARAMETER: [none, + ,   , +n ,    ,   ,   ,   ] SC

def test_no_leading_parameter():
    simple_edit_test("sa/t/abc/sc/t/", "def\n", "abcdef\n")

def test_plus_leading_parameter():
    simple_edit_test("sa/t/abc/+sc/t/", "def\n", "abcdef\n")

def test_pint_leading_parameter():
    simple_edit_test("sa/t/abc/2sc/t/", "def\n", "abcabcdef\n")

def test_no_leading_parameter_deref():
    simple_edit_test("sa/t1/t2/sa/t2/abc/sc/$t1$/", "def\n", "abcdef\n")

def test_no_leading_parameter_deref_2():
    simple_edit_test("2a>jm<a@sd/t/i/$t$/", "abc\ndef\nghi\n", "abc\ndef\nghiabc\ndef\nghi\n")
