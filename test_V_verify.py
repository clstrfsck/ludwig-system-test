from systest import simple_pexpect_test

#  LEADING PARAMETER: [none,   ,   ,    ,    ,   ,   ,   ] V

def test_no_leading_parameter_yes():
    cmd = "v&Yes?&[i/yes/:i/no/]"
    simple_pexpect_test("\\exludwig\ry\\q", cmd, f"yes{cmd}\n")

def test_no_leading_parameter_no():
    cmd = "v&Yes?&[i/yes/:i/no/]"
    simple_pexpect_test("\\exludwig\rn\\q", cmd, f"no{cmd}\n")

def test_no_leading_parameter_always():
    cmd = "3(v&Yes?&[i/yes/:i/no/])"
    simple_pexpect_test("\\exludwig\ra\\q", cmd, f"yesyesyes{cmd}\n")

def test_no_leading_parameter_quit():
    cmd = "3(v&Yes?&[i/yes/:i/no/])"
    simple_pexpect_test("\\exludwig\rqx\\q", cmd, f"x{cmd}\n")
