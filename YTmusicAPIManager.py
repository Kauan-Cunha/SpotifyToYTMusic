from ytmusicapi import YTMusic, OAuthCredentials
import json

class YTmusicAPIManager():
    def __init__(self):
        self.ytmusic = YTMusic("browser.json")


    def get_controller(self):
        """
        RETURN: return api controller (full access to ytmusicapi)
        """
        return self.ytmusic

    def search(self, str_query):
        """
        RETURN: list of yt videos retrieved in query
        """
        return self.ytmusic.search(str_query)
    
    def create_playlist(self, title:str, description:str, privacy_stats = "PRIVATE"):
        """
        RETURN: ID of YT playlist        
        """
        return self.ytmusic.create_playlist(title, description, privacy_status=privacy_stats.upper())

    
    def add_track_playlist(self, playlist_id: str, video_id:str):
        return self.ytmusic.add_playlist_items(playlist_id, [video_id], duplicates=True)