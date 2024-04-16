import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from googleapiclient.discovery import build
import json
import glob

youtube = build(
    "youtube", "v3", developerKey="")

offset = 0
token = ""
def get_videos(youtube, token, offset):
    request = youtube.search().list(
        part="snippet",
        q="como ganar dinero ahorro ahorrar",
        maxResults=50,
        order="date",
        type="video",
        regionCode="es",
        pageToken=token
    )
    response = request.execute()

    with open(f'yt_videos_{offset}.json', 'w', encoding="utf-8") as f:
        json.dump(response, f)

    if offset == 5:
        pass

    else:
        if response["nextPageToken"] == None:
            print("Final")
            pass

        else:
            offset = offset + 1
            print("Nova petició")
            token = response["nextPageToken"]
            get_videos(youtube, token, offset)

get_videos(youtube, token, offset)

