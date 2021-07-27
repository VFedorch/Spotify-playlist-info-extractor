import requests
import json

access_token = "YOUR_OAUTH_TOKEN"

playlist_id = "PLAYLIST_ID"
market = "ES"
fields = "items(track(artists(name)%2Cname%2Calbum(name)))"
limit = "100"
offset = "0"

url = "https://api.spotify.com/v1/playlists/"+ playlist_id +"/tracks?market="+market+"&fields="+fields+"&limit="+limit+"&offset="+offset

response = requests.get(
                        url, 
                        headers = {
                                    'Accept': 'application/json',
                                    'Content-Type': 'application/json',
                                    'Authorization': 'Bearer ' + access_token
                                    }
                        )
json_response = response.json()
# print(json_response)

print("NAME - ARTIST - ALBUM")

for item in json_response["items"]:
    
    track_name = item["track"]["name"]
    album_name = item["track"]["album"]["name"]
    artist_name=""

    for artist in item["track"]["artists"]:
        artist_name = artist["name"]
        ', '.join(artist_name)

    print(track_name+" - "+artist_name+" - "+album_name)
