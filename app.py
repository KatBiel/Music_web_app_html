import os
from flask import Flask, request, redirect, render_template
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import Album
from lib.artist_repository import ArtistRepository
from lib.artist import Artist
from lib.album_parameters_validator import AlbumParametersValidator

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
    first_album = albums[0]
    artist_id = first_album.artist_id
    artists = artist_repository.find_artist(artist_id)
    return render_template("albums/album_find.html", albums=albums, artists=artists)


@app.route('/albums/new')
def get_album_new():
    return render_template('albums/new.html')


@app.route('/albums', methods=['POST'])
def create_album():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)

    validator = AlbumParametersValidator(
        request.form['title'],
        request.form['release_year']
    )

    if not validator.is_valid():
        errors = validator.generate_errors()
        return render_template("albums/new.html", errors=errors)
        
    title = request.form['title']
    release_year = request.form['release_year']
    album = Album(None, title, release_year, 1)

    repository.create(album)
    return redirect(f"/albums/{album.id}")

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
# if __name__ == '__main__':
#     app.run(
#     debug=True, # Optional but useful for now
#     host="0.0.0.0" # Listen for connections directed _to_ any address
#     )
