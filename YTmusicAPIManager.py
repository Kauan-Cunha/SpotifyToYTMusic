from ytmusicapi import YTMusic, OAuthCredentials
from joblib import Parallel, delayed

class YTmusicAPIManager():
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
    
    def create_playlist(self, title:str, description:str, privacy_stats = "PRIVATE"):
        """
        RETURN: ID of YT playlist        
        """
        return self.ytmusic.create_playlist(title, description, privacy_status=privacy_stats.upper())

    
    def add_tracks_playlist(self, playlist_id: str, video_id: list[str]):
        return self.ytmusic.add_playlist_items(playlist_id, video_id, duplicates=True)
    
    def get_id_trackName(self, trackList: list[str]) -> list[str]:
        def _get_video_id(track):
            list_results = self.search(track)
            if len(list_results) != 0: 
                top_id = list_results[0]['videoId'] 
                print(track)
                return top_id

        
        parallel_obj = Parallel(n_jobs=-1, prefer='threads')
        videos_id = parallel_obj(delayed(_get_video_id)(track) for track in trackList)  #returns the list of id for names
        videos_id = [vid for vid in videos_id if vid is not None]
        return videos_id