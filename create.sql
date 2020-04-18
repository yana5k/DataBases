--------------------------------------

CREATE TABLE Artists(
    artist VARCHAR2(70) NOT NULL PRIMARY KEY
);
-------------------------------------


CREATE TABLE Genres(
    genre VARCHAR2(30) NOT NULL PRIMARY KEY
);

-----------------------------------

CREATE TABLE AlbumInfo(
    id_album INT NOT NULL PRIMARY KEY 
    , artist VARCHAR2(70) NOT NULL REFERENCES Artists(artist)
    , album VARCHAR2(75) NOT NULL
    , year INT NOT NULL
);

-----------------------------------


CREATE TABLE AlbumGenre(
    id_album INT NOT NULL REFERENCES AlbumInfo(id_album)
    , genre VARCHAR2(30) NOT NULL REFERENCES Genres(genre)
    , CONSTRAINT albumgenre_pk PRIMARY KEY(id_album, genre)
);


