import SpotifyAPIManager as sAPI
import YTmusicAPIManager as ytAPI
import TransferClass as tAPI
import json

def main():
    tranferConn = tAPI.TransferaClass('spo', 'yt')
    tranferConn.transfer_saved_tracks(input("Qual o nome da playlist?"))
    
if __name__ == '__main__':
    main()