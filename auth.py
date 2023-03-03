import spotipy
from flask import session
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

load_dotenv()

SPOTIPY_CLIENT_ID = os.environ.get('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.environ.get('SPOTIPY_CLIENT_SECRET')
SPOTIPY_REDIRECT_URI = os.environ.get('SPOTIPY_REDIRECT_URI')


def create_spotify_oauth():
    sp = SpotifyOAuth(
        client_id = SPOTIPY_CLIENT_ID,
        client_secret = SPOTIPY_CLIENT_SECRET,
        scope = 'user-read-email user-read-private'
    )
    return sp