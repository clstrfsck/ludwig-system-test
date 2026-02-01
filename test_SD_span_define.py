import re
from systest import simple_edit_test, multi_file_edit_test

# LEADING PARAMETER: [none,   , - , +n ,    ,   ,   ,   ] SD

def test_no_leading_parameter():
    simple_edit_test(">jm<jsd/asd/zci/a/st/asd/", "should be transferred\n", "\nashould be transferred\n")

def test_leading_parameter_minus():
    infile = "should be available\n"
    multi_file_edit_test(
        ">jm<jsd/asd/-sd/asd/st/asd/[:7ji/not /]",
        {
            "test_file": infile
        },
        {
            "test_file": "should not be available\n",
            "test_file~1": infile
        },
        [
            r"\A" + re.escape(f"No such span."),
            re.escape(f"/test_file closed (1 line read).") + r"\Z",
            re.escape(f"/test_file created (1 line written).") + r"\Z"
        ]
    )
