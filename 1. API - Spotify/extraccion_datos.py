import spotipy
import spotipy.util as util
import pandas as pd

#credenciales para acceder a la información.
scope = 'user-library-read'
username = 'oscarffu'
#Con prompt_for_user_token y los parametros indicados obtenemos el token que nos permite acceder a la información.
token = util.prompt_for_user_token(username, scope, client_id='cdaa8da2cd434db7b633299fd2597500', client_secret='d672cb475d5644279383080be8215280',redirect_uri='https://www.google.com/')
# Playlist Colombia Top 50.
id_playlist = '37i9dQZEVXbOa2lmxNORXQ'

if token:
    sp = spotipy.Spotify(auth=token)
    #Extraemos la información y la almacenamos en una variable.
    results = sp.user_playlist_tracks(username, id_playlist)
    need = []
    #Iteramos en el JSON y extraemos la información especifica que necesitamos. El nombre del artista y el nombre de la cancion.
    for i, item in enumerate(results['items']):
        track = item['track']
        need.append((track['artists'][0]['name'], track['name']))
    #Almacenamos la información en un DataFrame con el framework Pandas.
    top_colombian_songs = pd.DataFrame(need, columns=('Artists Name', 'Song Name'))
    genre = []
    #Ver Nota 1 en Readme
    for artist in top_colombian_songs['Artists Name']:
        g = sp.search(artist, type='artist')
        genre.append(g['artists']['items'][0]['genres'])

#Creamos una nueva columna con la información del género musical.
top_colombian_songs['Genres'] = genre
#Exportamos la data a un archivo CSV.
top_colombian_songs.to_csv('Songs.csv', sep=';', encoding='utf-8', index=False)
print("Archivos guardados con exito!")
