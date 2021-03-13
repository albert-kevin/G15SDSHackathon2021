import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
# import keys

ultra = pd.read_csv("ultra.csv")

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="f93a1fbf63074ec3b110cc58b86957dc",
                                                           client_secret="bee7864fda474acdbfc4789c59d53ec1"))

for artistTitre in ultra[['Artiste', 'Titre']].agg(''.join, axis=1):
    response = sp.search(q=artistTitre, limit=1)
