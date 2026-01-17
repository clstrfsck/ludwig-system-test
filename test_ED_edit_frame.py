from systest import multi_file_edit_test

# LEADING PARAMETER: [none,   ,   ,    ,    ,   ,   ,   ] ED

def test_no_leading_parameter():
    multi_file_edit_test(
        "ed/asd/ersi",
        { "zz": "line1\nline2\nline3\n" },
        { "zz": "line1\nline2\nline3\n" },
        [
            '^$', '^$', '^$',
            '^Spans$',
            '^=====$',
            '^          <none>$',
            '^$',
            '^Frames$',
            '^======$',
            '^ASD *$',
            '^$', '^$', '^$',
            '^Frames$',
            '^======$',
            '^COMMAND *$',
            '^$', '^$', '^$',
            '^Frames$',
            '^======$',
            '^HEAP *$',
            '^$', '^$', '^$',
            '^Frames$',
            '^======$',
            '^LUDWIG *$',
            '^  Output: .*/test_file$',
            '^$', '^$', '^$',
            '^Frames$',
            '^======$',
            '^OOPS *$',
        ]
    )
