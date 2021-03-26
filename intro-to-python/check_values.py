def test_with_empty_string():
    assert type(my_string) == str, "Should be a String"
    
    if not len(my_string):
        assert is_correct == False, "Should be False"

def test_with_valid_string():
    assert type(my_string) == str, "Should be a String"
    
    if len(my_string):
        assert is_correct == True, "Should be True"

if __name__ == "__main__":
    # change this value and test your code
    my_string = None
    is_correct = None


    my_string = 'Milind'

    if my_string != None:
        is_correct = True
    else:
        is_correct = False

    print(my_string, is_correct)