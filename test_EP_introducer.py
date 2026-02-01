from systest import simple_pexpect_test

# This test ensures that the command introducer can be changed.

def test_command_introducer_change():
    simple_pexpect_test("\\epc=/\r/2d/q", "unsuccessful", "successful\n")

def test_command_introducer_change_allows_backslash():
    simple_pexpect_test("\\epc=/\r/2d\\/q", "unsuccessful", "\\successful\n")
