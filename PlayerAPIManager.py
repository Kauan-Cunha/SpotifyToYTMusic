from abc import ABC, abstractmethod

class PlayerAPIManager(ABC):
    @abstractmethod
    def get_liked_tracks(self) -> list[str]:
        """
            Return the list of all liked tracks name(str) + artist_name_0(str) + artist_name_1(str) + ... 
        """
        pass

    @abstractmethod
    def search(self, q: str, filter: str):
        """
            Searches for an item (usually a track/song), remember to specify the type beforehand.
        """
        pass

    @abstractmethod
    def get_tracksId(self, trackList: list[str]) -> list[str]:
        """
            Returns the a list of tracks_id from a list of track_names 
        """
        pass

    @abstractmethod
    def add_tracks(self, playlist_id: str, tracks_id: list [str]):
        """
            Add a list of tracks (id) into a playlist (id).
            
            Since each track process depends on doing multiple sequential HTTP requests, it's ideal to parall 
        """
        pass

    @abstractmethod
    def create_playlist(self, title: str, description: str, privacy_stats:str) -> str:
        """
            Creates playlist with given title, description and privacy_stats.
            RETURNS: playlist id
        """
        pass
