# Fer el mateix procés d'obtenció pero no partir desde un ID sino desde una playlist (punt d'inici
# 1) Documetnarnos si Spotipy té alguna funció per fe-ho
# 2) Obtenir dades en excel de les dades basiqeus
# 3) Generar el graph


import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import pandas as pd

api_client_id = ""
api_client_secret = ""

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(api_client_id,api_client_secret))

artist_id = '0sKBEhvr6hz7Wpptw0fY8U'
results = spotify.playlist_items('1vs3kcfG3nJR8tKEILrOya')

print(results)



df = pd.DataFrame(results, columns = [])

df.to_csv("database.csv", sep=",", index=False)
