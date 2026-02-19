import requests as r

class SpotifyAPIManager():
    def __init__(self):
        self.token = None

    def is_token_valid(self):
        return False if self.token is None else self.token["expires_in"] >= 90  #arbitrary low expiring sec so we dont keep requesting 

    def get_token_spotify(self):
        if (self.is_token_valid()):
            return self.token

        URL = 'https://accounts.spotify.com/api/token'
        header = {'Content-Type' : 'application/x-www-form-urlencoded'}
        body = f'grant_type=client_credentials&client_id=e10e6fdc109043a2a1c0d866d501b335&client_secret=614c20475059428aa5add3e4c7434821'

        response = r.request('POST',url=URL, headers=header, data= body)
        response.raise_for_status()      #raise an arror if http status is 4xx or 5xx
        
        return response.json()    #returns a dict with the value in json response
        
    def spotify_request(self, endpoint:str) -> dict:
        access_token = self.get_token_spotify()["access_token"]
        url = 'https://api.spotify.com/v1/' + endpoint
        header = {'Authorization' : f'Bearer  {access_token}'}

        response = r.request('GET', url=url, headers=header)
        response.raise_for_status()

        return response.json();