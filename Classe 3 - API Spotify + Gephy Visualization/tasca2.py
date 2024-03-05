# Fer el mateix procés d'obtenció pero no partir desde un ID sino desde una playlist (punt d'inici
# 1) Documetnarnos si Spotipy té alguna funció per fe-ho
# 2) Obtenir dades en excel de les dades basiqeus
# 3) Generar el graph

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import pandas as pd

api_client_id = ""
api_client_secret = ""

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(api_client_id, api_client_secret))
result_playlist = spotify.playlist_items('37i9dQZF1DX7fvgalTu2lg')

llista_definitiva = []

for e in result_playlist['items']:
    for artist_data in e['track']['artists']:
        artist_id = artist_data['id']
        artist_name = artist_data['name']
        print(artist_name)

        def get_related(artist_id):
            resposta = spotify.artist_related_artists(artist_id)
            return resposta

        result = get_related(artist_id)

        llista_de_relacionats = []

        for artist in result['artists']:
            artista = {}
            artista['origen'] = artist_name
            artista["desti"] = artist["name"]
            artista["generes"] = artist["genres"]
            artista["id"] = artist["id"]
            llista_de_relacionats.append(artista)

        llista_definitiva.extend(llista_de_relacionats)

llista_tuples = []

for i in llista_definitiva:
    source = i["origen"]
    target = i["desti"]
    tupla = (source, target)
    llista_tuples.append(tupla)

for i in llista_definitiva:
    for g in i["generes"]:
        source = i["desti"]
        target = g
        tupla = (source, target)
        llista_tuples.append(tupla)

df = pd.DataFrame(llista_tuples, columns=["source", "target"])

print(df)
df.to_csv("graf_playlist.csv", sep=",", index=False)
