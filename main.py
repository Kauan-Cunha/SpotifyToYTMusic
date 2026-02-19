import SpotifyAPIManager as sAPI

def main():
    manager = sAPI.SpotifyAPIManager()

    response = manager.spotify_request('albums/4aawyAB9vmqN3uQ7FjRGTy')
    print(response)



if __name__ == '__main__':
    main()