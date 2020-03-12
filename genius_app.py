from flask import Flask
import requests
import json


app = Flask(__name__)


@app.route('/artist/<artist>')
def artist_songs(artist):
    client_access_token = 'YourClientAccessToken'
    base_url = 'https://api.genius.com'
    path = 'search/'
    request_uri = '/'.join([base_url, path])
    params = {'q': artist}
    token = 'Bearer {}'.format(client_access_token)
    headers = {'Authorization': token}
    r = requests.get(request_uri, params=params, headers=headers)
    parsed = json.loads(r.text)
    results = parsed['response']['hits']
    songs = []
    for result in results:
        music = result['result']['title']
        songs.append(music)
    json_songs = json.dumps(songs)
    return json_songs
