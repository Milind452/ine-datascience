def test_final_text():
    assert text == "Learning Python with INE"

if __name__ == "__main__":
    string_1 = "Learning Python"
    string_2 = "with INE"

    # Final text should be:
    # "Learning Python with INE"
    text = string_1 + " " + string_2


    test_final_text()