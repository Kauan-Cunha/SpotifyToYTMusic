from ytmusicapi import YTMusic, OAuthCredentials
from joblib import Parallel, delayed
from backend.app.managers.PlayerAPIManager import PlayerAPIManager

class YTmusicAPIManager(PlayerAPIManager):
    def __init__(self):
        self.ytmusic = YTMusic("browser.json")

    def get_controller(self):
        """
        RETURN: return api controller (full access to ytmusicapi)
        """
        return self.ytmusic

    def search(self, str_query, filter = 'songs'):
        """
        RETURN: list of yt videos retrieved in query
        """
        return self.ytmusic.search(str_query, filter=filter)
    
    def create_playlist(self, title:str, description:str, privacy_stats = "PRIVATE") -> str:
        """
        RETURN: ID of YT playlist        
        """
        return self.ytmusic.create_playlist(title, description, privacy_status=privacy_stats.upper())

    
    def add_tracks(self, playlist_id: str, tracks_id: list[str]) -> None:
        self.ytmusic.add_playlist_items(playlist_id, tracks_id, duplicates=True)
    
    def get_tracksId(self, trackList: list[str]) -> list[str]:
        def _get_video_id(track):
            list_results = self.search(track)
            if len(list_results) != 0: 
                top_id = list_results[0]['videoId'] 
                return top_id

        
        parallel_obj = Parallel(n_jobs=-1, prefer='threads')
        videos_id = parallel_obj(delayed(_get_video_id)(track) for track in trackList)  #returns the list of id for names
        videos_id = [vid for vid in videos_id if vid is not None]
        return videos_id
    
    def get_liked_tracks(self) -> list[str]:
        n_tracks = int(self.ytmusic.get_playlist('LM', limit=1)['trackCount'])
        trackItens = self.ytmusic.get_playlist("LM", limit = n_tracks)['tracks']

        name_list = list()
        for track in trackItens:
            name_list.append(track['title'] + " " + " ".join(artist['name'] for artist in track['artists']))

        return name_list