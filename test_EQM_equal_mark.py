from systest import simple_edit_test, syntax_error

# LEADING PARAMETER: [none, + , - ,    ,    , > , < ,   ] EQM

def test_no_leading_parameter_success():
    simple_edit_test("meqm/1/[i/yes/:i/no/]", "abc\n", "yesabc\n")

def test_no_leading_parameter_fail():
    simple_edit_test("mjeqm/1/[i/yes/:i/no/]", "abc\n", "anobc\n")

def test_plus_leading_parameter_success():
    simple_edit_test("m+eqm/1/[i/yes/:i/no/]", "abc\n", "yesabc\n")

def test_minus_leading_parameter_success():
    simple_edit_test("mj-eqm/1/[i/yes/:i/no/]", "abc\n", "ayesbc\n")

def test_minus_leading_parameter_fail():
    simple_edit_test("jm-eqm/1/[i/yes/:i/no/]", "abc\n", "anobc\n")

def test_gt_leading_parameter_before_mark():
    simple_edit_test("jm-j>eqm/1/[i/yes/:i/no/]", "abc\n", "noabc\n")

def test_gt_leading_parameter_at_mark():
    simple_edit_test("jm>eqm/1/[i/yes/:i/no/]", "abc\n", "ayesbc\n")

def test_gt_leading_parameter_after_mark():
    simple_edit_test("jmj>eqm/1/[i/yes/:i/no/]", "abc\n", "abyesc\n")

def test_lt_leading_parameter_before_column():
    simple_edit_test("jm-j<eqm/1/[i/yes/:i/no/]", "abc\n", "yesabc\n")

def test_lt_leading_parameter_at_column():
    simple_edit_test("jm<eqm/1/[i/yes/:i/no/]", "abc\n", "ayesbc\n")

def test_lt_leading_parameter_after_column():
    simple_edit_test("jmj<eqm/1/[i/yes/:i/no/]", "abc\n", "abnoc\n")

def test_equals_mark():
    simple_edit_test("i/hello/=j=deqm/%/[i/yes/:i/no/]>eqm/=/[i/yes/:i/no/]", "abc\n", "yesyesabc\n")