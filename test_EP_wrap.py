from systest import simple_pexpect_test

# This test ensures that the command introducer can be changed.

def test_ep_wrap_1():
    simple_pexpect_test(
        "\\epm=(2,10)\r\\epo=w\r This is a not very wide screen which wraps incessantly\\q",
        "",
        " This is a\n not very\n wide\n screen\n which\n wraps\n incessant\n ly\n"
    )
