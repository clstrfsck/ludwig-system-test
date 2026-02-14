from systest import simple_edit_test

# LEADING PARAMETER: [none,   ,   ,    ,    ,   ,   ,   ] ST

def test_no_leading_parameter_frame():
    simple_edit_test("ed/test/i/span info/erst/test/", "abc\n", "span info\nabc\n")

def test_no_leading_parameter_span():
    simple_edit_test("g/span/=sd/test/<ast/test/i/|/", "this is a >span<\n", "span|this is a ><\n")
