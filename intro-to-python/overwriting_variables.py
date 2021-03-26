def test_overwrite():
    assert old_variable == "hats"
    assert another_old_variable != 42

if __name__ == "__main__":
    old_variable = "pants"
    another_old_variable = 42

    # Overwrite "old_variable" and change it's value from "pants" to "hats"
    old_variable = "hats"

    # Overwrite "another_old_variable" to something different on the line below
    another_old_variable = 100


    test_overwrite()