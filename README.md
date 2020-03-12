It's developed using Flask

How to install it locally (supposing you have git and python >= 3.7 installed):

```console
git clone https://github.com/guilhermegouw/genius_songs.git
cd genius_songs
python -m pip install pipenv
pipenv install
```

Now that all dependencies are installed

You will need a Client access token from genius api.\
You can get one here: https://docs.genius.com/\
Click on the 'API Client management page' link, fill the form and you are ready to go.

At the console:
```console
export FLASK_APP=genius_app.py
flask run
```

The application is pretty simple:\
In genius_app.py file insert the Client access token
```console
    client_access_token = 'YourClientAccessToken'
```
Open your browser and insert: http://127.0.0.1:5000/artist/artist_name
\
The browser will return the top 10 songs of the artist of your choice.

Enjoy!