import cx_Oracle


username = 'system'
password = '1234567890'
databaseName = 'localhost/xe'

connection = cx_Oracle.connect(username, password, databaseName)
cursor = connection.cursor()

query = '''
SELECT genres.genre, COUNT(id_album) AS albums
FROM genres
LEFT JOIN albumgenre ON genres.genre = albumgenre.genre
GROUP BY genres.genre
'''
cursor.execute(query)
print('')
print('First task')
print('|genre         |albums     ')
print('-'*30)
row = cursor.fetchone()
while row:

    print("|{:20}|{}".format(row[0], row[1]))
    row = cursor.fetchone()

print('')

"""
second task
"""
query = '''
SELECT albuminfo.artist,
    ROUND(COUNT(albuminfo.album)/(SELECT COUNT(albuminfo.album)
    FROM AlbumInfo
    JOIN AlbumGenre ON albuminfo.id_album = albumgenre.id_album
    WHERE albumgenre.genre = 'Rock')*100, 2) AS ratio
FROM AlbumInfo
JOIN AlbumGenre ON albuminfo.id_album = albumgenre.id_album
WHERE albumgenre.genre = 'Rock'
GROUP BY albuminfo.artist
'''
cursor.execute(query)
print('Second task')
print('|artist         |ratio     ')
print('-'*30)

row = cursor.fetchone()
while row:

    print("|{:20}|{}".format(row[0], row[1]))
    row = cursor.fetchone()

print('')


"""
Third task
"""
query = '''
SELECT albuminfo.year, COUNT(albuminfo.album) AS rock_albums
FROM albuminfo
JOIN albumgenre ON albuminfo.id_album = albumgenre.id_album
WHERE albumgenre.genre = 'Rock'
GROUP BY albuminfo.year
'''
cursor.execute(query)
print('Third task')
print('|year         |rock_albums ')
print('-'*25)

row = cursor.fetchone()
while row:

    print("|{:10}|{}".format(row[0], row[1]))
    row = cursor.fetchone()

print('')

