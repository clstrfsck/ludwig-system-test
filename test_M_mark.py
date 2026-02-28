from systest import simple_edit_test, failed_edit

# LEADING PARAMETER: [none, + , - , +n , -n ,   ,   ,   ] M

def test_no_leading_parameter():
    simple_edit_test("13jm<a@ji/|/", "abcdefghijklmnopqrstuvwxyz\n", "abcdefghijklm|nopqrstuvwxyz\n")

def test_all_leading_parameters():
    for i in range(1, 10):
        simple_edit_test(f"13j{i}m<a@{i}ji/|/", "abcdefghijklmnopqrstuvwxyz\n", "abcdefghijklm|nopqrstuvwxyz\n")

def test_minus_leading_parameters():
    for i in range(1, 10):
        simple_edit_test(f"13j{i}m<a-{i}m@j[i/yes/:i/no/]", "abcdefghijklmnopqrstuvwxyz\n", "noabcdefghijklmnopqrstuvwxyz\n")
