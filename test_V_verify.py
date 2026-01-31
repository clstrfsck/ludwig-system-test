from systest import simple_pexpect_test

#  LEADING PARAMETER: [none,   ,   ,    ,    ,   ,   ,   ] V

def test_no_leading_parameter():
    simple_pexpect_test("\\exludwig\ry\\q", "v&Yes?&[i/yes/:i/no/]", "yesv&Yes&^[i/yes/:i/no/]")
