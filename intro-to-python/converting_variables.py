def test_types():
    assert type(a_string) == str, 'Not a String'
    assert type(an_integer) == int, 'Not an Int'
    assert type(a_float) == float, 'Not a Float'
    assert type(a_bool) == bool, 'Not a Bool'

if __name__ == "__main__":
    a_string = 125
    an_integer = "10"
    a_float = "5.2"
    a_bool = 1

    a_string = str(a_string)
    an_integer = int(an_integer)
    a_float = float(a_float)
    a_bool = bool(a_bool)