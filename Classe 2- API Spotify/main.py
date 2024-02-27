# Problema: Volem un codi que recomani nous artistes d'spotify a partir d'un artista

import spotipy
import json
import pandas as pd

from spotipy.oauth2 import SpotifyClientCredentials

api_client_id = "0cac484801d54853ad37b3d5ecf06bd3"
api_client_secret = "badb887d0d214539943d06858a67afd9"

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(api_client_id,api_client_secret))

artist_id = '7ltDVBr6mKbRvohxheJ9h1'
results = spotify.artist_related_artists(artist_id)

artists = results['artists']

llista_artistes = []

for a in artists:
    name = a['name']
    id = a['id']
    followers = a['followers']['total']
    enlace = a['external_urls']['spotify']
    popularity = a['popularity']
    tipo = a['type']
    uri = a['uri']
    href = a['href']

    genres = ', '.join(a['genres'])
    images_list = ', '.join(image['url'] for image in a['images'])


    frame = pd.DataFrame({
        "Nom": name,
        "Tipus": tipo,
        "Followers": followers,
        "Link": enlace,
        "Popularitat": popularity,
        "Referencia": href,
        "Generes": genres,
        "Imatges": images_list,


    }, index=[0])
    llista_artistes.append(frame)


for i in artists:
    artist_id_related = i['id']
    results2 = spotify.artist_related_artists(artist_id_related)
    artists_related = results2['artists']
    for a in artists_related:

        name = a['name']
        id = a['id'],
        followers = a['followers']['total']
        enlace = a['external_urls']['spotify']
        popularity = a['popularity']
        tipo = a['type']
        uri = a['uri']
        href = a['href']
        genres = ','.join(a['genres'])
        images_list = ','.join(image['url'] for image in a['images'])

        frame = pd.DataFrame({
            "Nom": name,
            "Tipus": tipo,
            "Followers": followers,
            "Link": enlace,
            "Popularitat": popularity,
            "Referencia": href,
            "Generes": genres,
            "Imatges":images_list


        }, index=[0])

        llista_artistes.append(frame)

    final = pd.concat(llista_artistes)
    print(final)
    final.to_excel("dataset.xlsx")


# MOSTRAR RESULTADOS EN UN JSON LIMPIO Y FORMATO OK
with open('data_clean.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=4)


