from systest import simple_edit_test

# LEADING PARAMETER: [none, + ,   , +n ,    , > ,   ,   ] ZL

def test_no_leading_parameter():
    simple_edit_test(">jzli/m1/", "abc\nb\n", "abm1c\nb\n")

def test_plus_leading_parameter():
    simple_edit_test(">jzli/m1/", "abc\nb\n", "abm1c\nb\n")

def test_positive_leading_parameter():
    simple_edit_test(">j2zli/m1/", "abc\nb\n", "am1bc\nb\n")

def test_pindef_leading_parameter():
    simple_edit_test(">j>zli/m1/", "abc\nb\n", "m1abc\nb\n")

def test_pindef_leading_parameter_at_margin():
    simple_edit_test("ep/m=(2,10)/j>zl[i/yes/:i/no/]", "abc\nb\n", "ayesbc\nb\n")

def test_pindef_leading_parameter_beyond_margin():
    simple_edit_test("ep/m=(2,10)/>j>zl[i/yes/:i/no/]", "abc\nb\n", "ayesbc\nb\n")

def test_pindef_leading_parameter_fail():
    simple_edit_test("ep/m=(2,10)/>zl[i/yes/:i/no/]", "abc\nb\n", "noabc\nb\n")
