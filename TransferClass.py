import YTmusicAPIManager as ytAPI
import SpotifyAPIManager as sAPI

class TransferaClass():
    def __init__(self, origin: str, destine: str):
        self.ytConn = ytAPI.YTmusicAPIManager()
        self.spConn = sAPI.SpotifyAPIManager()

        #checks if type is right (both str)
        if type(origin) != str or type(destine) != str:
            raise TypeError("'Origin' and 'destine' args must be string type")
        
        #checks if both the choices are valid choices
        if not (self._valid_choice(destine) and self._valid_choice(origin)):
            raise ValueError("'Origin' and 'Destine' args values must be a valid choice")

        self.origin = origin
        self.destine = destine

    def _valid_choice(self, choice : str, options = ['SPOTIFY', 'YTMUSIC', 'YT', 'YOUTUBE']):
        return any([x.startswith(choice.upper()) and len(choice)>1  for x in options])  


    def spotify_to_youtube(self, destine_name):
        playlistId = self.ytConn.create_playlist(destine_name, 'Playlist auto created by MoveMusic  [from SPOTIFY to YOUTUBE]')
        trackName_list = self.spConn.get_liked_tracks() #list of names of all tracks
        
        #itero sobre eles e pesquiso 
        for track in trackName_list:
            video_id = self.ytConn.search(track)[0]['videoId']
            self.ytConn.add_track_playlist(playlist_id=playlistId, video_id=video_id) #i dont care about the reponse json (For now)
            print(track)

            
    def youtube_to_spotify(self):
        pass

    def transfer_saved_tracks(self, destine_name: str):
        if self._valid_choice(self.destine, options = ['YTMUSIC', 'YOUTUBE']) and self._valid_choice(self.origin, options=['SPOTIFY']):
            self.spotify_to_youtube(destine_name=destine_name)