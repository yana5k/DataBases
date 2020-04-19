
-- ----Запит 1:
-- вивести жанри та загальну кількість альбомів на кожен жанр
-- Візуалізація: стовпчикова діаграма.

SELECT genres.genre, COUNT(id_album) AS albums
FROM genres
LEFT JOIN albumgenre ON genres.genre = albumgenre.genre
GROUP BY genres.genre;
---------------------------------------------------------------------------

-- Запит 2:
-- вивести виконавців та % їхніх альбомів відносно альбомів інших виконавців у жанрі Rock
-- Візуалізація: секторна діаграма

SELECT albuminfo.artist,
    ROUND(COUNT(albuminfo.album)/(SELECT COUNT(albuminfo.album)
    FROM AlbumInfo
    JOIN AlbumGenre ON albuminfo.id_album = albumgenre.id_album
    WHERE albumgenre.genre = 'Rock')*100, 2) AS ratio
FROM AlbumInfo
JOIN AlbumGenre ON albuminfo.id_album = albumgenre.id_album
WHERE albumgenre.genre = 'Rock'
GROUP BY albuminfo.artist;
---------------------------------------------------------------------------

-- Запит 3: динаміка популярності жанру 'Rock' (графік залежності кількості альбомів від року)
-- Візуалізація: графік залежності

SELECT albuminfo.year, COUNT(albuminfo.album) AS rock_albums
FROM albuminfo
JOIN albumgenre ON albuminfo.id_album = albumgenre.id_album
WHERE albumgenre.genre = 'Rock'
GROUP BY albuminfo.year;
---------------------------------------------------------------------------
