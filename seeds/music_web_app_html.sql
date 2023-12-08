DROP TABLE IF EXISTS books;
DROP SEQUENCE IF EXISTS books_id_seq;

DROP TABLE IF EXISTS artists;
DROP SEQUENCE IF EXISTS artists_id_seq;

DROP TABLE IF EXISTS albums;
DROP SEQUENCE IF EXISTS albums_id_seq;


CREATE SEQUENCE IF NOT EXISTS albums_id_seq;
CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    title text,
    release_year int,
    artist_id int
);

CREATE SEQUENCE IF NOT EXISTS artists_id_seq;
CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    name text,
    genre text
);

INSERT INTO albums (title, release_year, artist_id) VALUES ('Voyage', 2022, 1);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Surfer Rosa', 1988, 1);


INSERT INTO artists (name, genre) VALUES ('Pixies', 'Rock');
INSERT INTO artists (name, genre) VALUES ('ABBA', 'Pop');
INSERT INTO artists (name, genre) VALUES ('Taylor Swift', 'Pop');;
INSERT INTO artists (name, genre) VALUES ('Nina Simone', 'Jazz');
