import pickle
import pandas as pd
from flask import Flask, request, render_template, jsonify
from ..web_functions import WebFunctionHandler


# with open('.pkl') as f:
#     model = pickle.load(f)

app = Flask(__name__, static_url_path="")

wfh = WebFunctionHandler()

@app.route('/')
def index():
    """Return the main page."""
    # all_songs = db.get_song_and_artist_names()
    artist_names = wfh.get_unique_artist_names()[:10].to_html()
    artists_selection = wfh.get_artist_selections(100)
    return render_template('index.html',
                                artist_names=artist_names,
                                artists_selection=artists_selection)

@app.route('/artist/<int:artist_id>')
def artist_songs(artist_id):
    """Return songs for an artist."""
    artist_songs = wfh.get_selector_for_songs(artist_id)
    return render_template('index.html',
                                artist_songs=artist_songs)
    



# @app.route('/recommendations/<id>')   
# def recommendations(id):
#     recs = db.get_recommendations(id)
#     return render_template('index.html',
#                                 recs=recs)

