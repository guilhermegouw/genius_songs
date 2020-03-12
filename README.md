It's developed using Flask

How to install it locally (supposing you have git and python >= 3.7 installed):

```console
git clone https://github.com/guilhermegouw/genius_songs.git
cd genius_songs
python -m pip install pipenv
pipenv install -d
```

Now that all dependencies are installed

You will need a Client access token from genius api.
You can get one here: https://docs.genius.com/
Click on the 'API Client management page' link, fill the form and you are ready to go.

At the console:
```console
export FLASK_APP=hello.py
flask run
```
