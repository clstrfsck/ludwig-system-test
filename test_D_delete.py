from systest import simple_edit_test
import pytest

# LEADING PARAMETER: [none, + , - , +n , -n , > , < , @ ] D

def test_no_leading_parameter():
    # Should delete the character at point
    simple_edit_test("di/m1/", "a\nb\n", "m1\nb\n")

def test_plus_leading_parameter():
    simple_edit_test("+di/m1/", "a\nb\n", "m1\nb\n")

def test_minus_leading_parameter():
    simple_edit_test("i/m1/-d", "a\nb\n", "ma\nb\n")

@pytest.mark.skip(reason="This test tests buggy behaviour fixed in the rust version")
def test_zero_leading_parameter():
    # I think this is buggy.  It should not modify the file.
    # This should work correctly:
    #     unmodified_test("0d", "a\nb\n")
    simple_edit_test("0d", "a\nb\n", "a\nb\n")

def test_positive_leading_parameter():
    simple_edit_test("3di/m1/", "abcd\nb\n", "m1d\nb\n")

def test_negative_leading_parameter():
    simple_edit_test("i/m1xyz/-3d", "a\nb\n", "m1a\nb\n")

def test_equals_leading_parameter():
    simple_edit_test("i/deleted/=di/m1/", "a\nb\n", "m1a\nb\n")

def test_equals_leading_parameter_2():
    simple_edit_test("2jj=d", "abc\n", "ab\n")

def test_bol_leading_parameter():
    simple_edit_test("i/deleted/<d", "abcd\nb\n", "abcd\nb\n")

def test_eol_leading_parameter():
    simple_edit_test("i/xyz/>d", "abcd\nb\n", "xyz\nb\n")
