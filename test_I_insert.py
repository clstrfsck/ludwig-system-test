from systest import simple_edit_test, syntax_error

# LEADING PARAMETER: [none, + ,   , +n ,    ,   ,   ,   ] I

def test_no_leading_parameter():
    simple_edit_test("i/insert/", "", "insert\n")

def test_plus_leading_parameter():
    simple_edit_test("+i/insert/", "", "insert\n")

def test_n_leading_parameter():
    simple_edit_test("3i/insert/", "", "insertinsertinsert\n")

def test_minus_leading_parameter():
    syntax_error("-i/insert/", "")

def test_insert_multi_line_2():
    simple_edit_test("i/insert\nline2/", "", "insert\nline2\n")

def test_insert_multi_line_3():
    simple_edit_test("i/insert\nline2\nline3/", "", "insert\nline2\nline3\n")
