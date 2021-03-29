import io

file_lines = 0
file_words = 0

with open('latin-lipsum.txt', 'r') as file:
    for line in file:
        if line != '\n':
            file_lines += 1
            file_words += len(line.split())


def test_file_content():
    assert isinstance(file_lines, int), "Should be Integer"
    assert file_lines == 100, "Wrong value"
    assert isinstance(file_words, int), "Should be Integer"
    assert file_words == 4500, "Wrong value"