from my_package.my_file import add_one

def test_add_one():
    tc_list = [
        (0, 1),
        (1, 2)
    ]

    for input, expected in tc_list:
        assert add_one(input) == expected
