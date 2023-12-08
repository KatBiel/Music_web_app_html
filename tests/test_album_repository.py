from lib.album_repository import AlbumRepository
from lib.album import Album

'''
When i call #all
I get all albums in the albums table
'''

def test_all(db_connection):
    db_connection.seed('seeds/music_web_app_html.sql')
    repository = AlbumRepository(db_connection)
    assert repository.all() == [
        Album(1, 'Voyage', 2022, 1),
        Album(2, 'Surfer Rosa', 1988, 1)
    ]

def test_create(db_connection):
    db_connection.seed('seeds/music_web_app_html.sql')
    repository = AlbumRepository(db_connection)
    album = Album(None, 'Test Title', 2000, 1)
    repository.create(album)
    assert repository.all() == [
        Album(1, 'Voyage', 2022, 1),
        Album(2, 'Surfer Rosa', 1988, 1),
        Album(3, 'Test Title', 2000, 1)
    ]