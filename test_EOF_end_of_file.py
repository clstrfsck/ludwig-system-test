from systest import simple_edit_test, syntax_error

# LEADING PARAMETER: [none, + , - ,    ,    ,   ,   ,   ] EOF

def test_no_leading_parameter_success():
    simple_edit_test(">aeof[i/yes/:i/no/]", "abc\n", "abc\nyes\n")

def test_no_leading_parameter_fail():
    simple_edit_test("eof[i/yes/:i/no/]", "abc\n", "noabc\n")

def test_plus_leading_parameter_success():
    simple_edit_test(">a+eof[i/yes/:i/no/]", "abc\n", "abc\nyes\n")

def test_minus_leading_parameter_success():
    simple_edit_test("-eof[i/yes/:i/no/]", "abc\n", "yesabc\n")

def test_minus_leading_parameter_fail():
    simple_edit_test(">a-eof[i/yes/:i/no/]", "abc\n", "abc\nno\n")
