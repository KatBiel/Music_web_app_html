import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import Album
from lib.artist_repository import ArtistRepository
from lib.artist import Artist

app = Flask(__name__)

@app.route('/albums')
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.all()
    return render_template("albums/index.html", albums=albums)

# @app.route('/albums/1') 
# def get_first_album():
#     connection = get_flask_database_connection(app)
#     repository = AlbumRepository(connection)
#     album = repository.find(1)
#     return render_template("albums/album_1.html", album=album)

@app.route('/albums/<int:id>') 
def get_first_album_with_an_id(id):
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    artist_repository = ArtistRepository(connection)
    albums = repository.find(id)
    return render_template("albums/album_find.html", albums=albums)

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
