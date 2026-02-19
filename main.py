import SpotifyAPIManager as sAPI
import json

def main():
    manager = sAPI.SpotifyAPIManager()

    request = manager.spotify_request('/me/tracks')

    with open('test.json', 'w') as f:
        json.dump(request, f)

if __name__ == '__main__':
    main()