import cx_Oracle
import chart_studio
##############################################
chart_studio.tools.set_credentials_file(username = 'yanna', api_key = 'vVVLEYx1RCef9YlfOUJU')

import plotly.graph_objects as go
import chart_studio.plotly as py
import chart_studio.dashboard_objs as dashboard
import re

def fileId_from_url(url):
	raw_fileID = re.findall("~[A-z.]+/[0-9]+", url)[0][1:]
	return raw_fileID.replace('/', ':')

username = 'SYSTEM'
password = 'Qweasd1!2233'
databaseName = 'localhost/xe'

connection = cx_Oracle.connect(username, password, databaseName)
cursor = connection.cursor()
#---------------------------------------------------
query = '''
SELECT genres.genre, COUNT(id_album) AS albums
FROM genres
LEFT JOIN albumgenre ON genres.genre = albumgenre.genre
GROUP BY genres.genre
'''
cursor.execute(query)

genres = []
albums = []

for record in cursor.fetchall():
	genres.append(record[0])
	albums.append(record[1])

bar = go.Bar(x = genres, y = albums)
bar_scheme = py.plot([bar], filename = 'lab21')

#----------------------------------------------------

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
artists = []
ratios = []

for record in cursor.fetchall():
	artists.append(record[0])
	ratios.append(record[1])

pie = go.Pie(labels = artists, values = ratios)
pie_scheme = py.plot([pie], filename = 'db22')


#---------------------------------------------------------------
query = '''
SELECT albuminfo.year, COUNT(albuminfo.album) AS rock_albums
FROM albuminfo
JOIN albumgenre ON albuminfo.id_album = albumgenre.id_album
WHERE albumgenre.genre = 'Rock'
GROUP BY albuminfo.year
ORDER BY albuminfo.year
'''
cursor.execute(query)

years = []
rock_albums = []

for record in cursor.fetchall():
	years.append(record[0])
	rock_albums.append(record[1])

scatter = go.Scatter(
	x= years,
	y = rock_albums
)

data = [scatter]
plot_scheme = py.plot(data, filename = 'db23')

my_board = dashboard.Dashboard()
bar_scheme_id = fileId_from_url(bar_scheme)
plot_scheme_id = fileId_from_url(plot_scheme)
pie_scheme_id = fileId_from_url(pie_scheme)

box_1 = {
	'type' : 'box',
	'boxType' : 'plot',
	'fileId' : bar_scheme_id,
	'title' : 'Запит 1'
}

box_2 = {
	'type' : 'box',
	'boxType' : 'plot',
	'fileId' : pie_scheme_id,
	'title' : 'Запит 2'
}

box_3 = {
	'type' : 'box',
	'boxType' : 'plot',
	'fileId' : plot_scheme_id,
	'title' : 'Запит 3'
}

my_board.insert(box_3)
my_board.insert(box_1, 'right', 1)
my_board.insert(box_2, 'above', 2)

py.dashboard_ops.upload(my_board, 'DB Lab 2')