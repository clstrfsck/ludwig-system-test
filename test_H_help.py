from systest import simple_pexpect_test

#  LEADING PARAMETER: [none,   ,   ,    ,    ,   ,   ,   ] H

def test_no_leading_parameter_yes():
    simple_pexpect_test("\\h\r\r\\d\\q", "abc\n", "bc\n", "Main Help Menu")
