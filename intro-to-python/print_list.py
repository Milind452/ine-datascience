def test_while():
    assert type(my_list) == list, "Should be a List"
    assert type(i) == int, "Should be an Integer"
    assert i == len(my_list), "Should print all list values"

if __name__ == "__main__":
    my_list = [True, 'Programming', 'Python', 'with', 'INE', 123]
    i = None


    i = len(my_list)
    x = 0
    while x < i:
        print(my_list[x])
        x += 1

    test_while()