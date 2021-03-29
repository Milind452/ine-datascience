import csv
from collections import Counter

artists = []
top_artists = []

with open('top-spotify-songs.csv', 'r') as file:
    reader = csv.reader(file)

    for line in reader:
        if line[0] == '0':
            continue
        artists.append(line[2])

count = Counter(artists)
count = {k: v for k, v in sorted(count.items(), key=lambda item: item[1], reverse = True)}
for i, item in enumerate(count):
    if i == 5:
        break
    top_artists.append((item, count[item]))


def test_artists():
    assert isinstance(artists, list), "Should be a list"
    assert len(artists) == 603, "Wrong artists count"
    assert artists[207] == 'Jewel', "Wrong values"
    assert artists[561] == 'Rita Ora', "Wrong values"
    assert artists[124] == 'Katy Perry', "Wrong values"

def test_top_artists():
    assert isinstance(top_artists, list), "Should be a list"
    assert len(top_artists) == 5, "Wrong artists count"
    assert top_artists[3] == ('Maroon 5', 15), "Wrong values"
