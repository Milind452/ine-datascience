def test_floats():
    assert one_tenth == 0.1
    assert one_half == 0.5
    assert pi == 3.14

def test_integers():
    assert one == 1
    assert seven == 7
    assert fourteen == 14
    assert a_hundred == 100
    assert minus_five == -5

if __name__ == "__main__":
    # Integers
    one = 1
    seven = 7
    fourteen = 14
    a_hundred = 100
    minus_five = -5

    # Floats
    one_tenth = 0.1
    one_half = 0.5
    pi = 3.14  # Hint: it's 3.14 ;)

    test_floats()
    test_integers()
