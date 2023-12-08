from lib.artist import Artist

def test_constructor():
    artist = Artist(1, "Test Artist", "Test Genre")
    assert artist.id == 1
    assert artist.name == "Test Artist"
    assert artist.genre == "Test Genre"

def test_equality():
    artist_1 = Artist(1, "Test Artist", "Test Genre")
    artist_2 = Artist(1, "Test Artist", "Test Genre")
    assert artist_1 == artist_2

def test_formatter():
    artist = Artist(1, "Test Artist", "Test Genre")
    assert str(artist) == "Artist(1, Test Artist, Test Genre)"