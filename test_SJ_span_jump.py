from systest import simple_edit_test

# LEADING PARAMETER: [none, + , - ,    ,    ,   ,   ,   ] SJ

def test_no_leading_parameter():
    simple_edit_test("g/span/=sd/test/<asj/test/i/|/", "this is a >span<\n", "this is a >span|<\n")

def test_plus_leading_parameter():
    simple_edit_test("g/span/=sd/test/<a+sj/test/i/|/", "this is a >span<\n", "this is a >span|<\n")

def test_minus_leading_parameter():
    simple_edit_test("g/span/=sd/test/<a-sj/test/i/|/", "this is a >span<\n", "this is a >|span<\n")
