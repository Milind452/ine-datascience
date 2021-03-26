def test_shorthand():
    assert change_me == 61, "Wrong value"

if __name__ == "__main__":
    change_me = 34

    # Use the shorthand to multiply change_me by 7 and store the result in change_me
    change_me *= 7

    # Now add 23 to change_me
    change_me += 23

    # Subtract 17 from change_me
    change_me -= 17

    # Divide change_me by 4
    change_me /= 4


    test_shorthand()