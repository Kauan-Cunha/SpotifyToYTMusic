import YTmusicAPIManager as ytAPI
import SpotifyAPIManager as sAPI
# from joblib import Parallel, delayed
from PlayerAPIManager import PlayerAPIManager

class TransferaClass():
    def __init__(self, origin: PlayerAPIManager, destine: PlayerAPIManager):
        self.destine = destine
        self.origin = origin


    def transfer_liked_tracks(self, destine_name: str):
        #Create a destine playlist in destine_player
        playlistId = self.destine.create_playlist(destine_name, 'Playlist auto created by MoveMusic')

        #Retrieve the liked tracks of connected origin_player profile
        trackName_list = self.origin.get_liked_tracks() 
        
        #Retriving destine_player track's id given a trackName_list
        tracks_id = self.destine.get_tracksId(trackName_list)

        #Add tracks to destine previosly created playlist
        self.destine.add_tracks(playlist_id=playlistId, tracks_id=tracks_id)