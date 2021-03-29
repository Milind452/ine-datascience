import json

user_fullnames = []

with open('users.json', 'r') as file:
    users = json.load(file)
    for user in users:
        user_fullnames.append(user['firstName'] + ' ' + user['lastName'])


def test_user_fullnames():
    assert isinstance(user_fullnames, list), "Should be a list"
    assert len(user_fullnames) == 5, "Wrong users count"
    assert user_fullnames[0] == "Krish Lee", "Wrong values"
    assert user_fullnames[3] == "devid neo", "Wrong values"