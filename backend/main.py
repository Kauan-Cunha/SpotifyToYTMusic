import backend.SpotifyAPIManager as sAPI
import backend.YTmusicAPIManager as ytAPI
import backend.TransferClass as tAPI
import json

def main():
    ytConn = ytAPI.YTmusicAPIManager()
    sConn  = sAPI.SpotifyAPIManager()

    tranferConn = tAPI.TransferaClass(ytConn, sConn)
    tranferConn.transfer_liked_tracks(input("Qual o nome da playlist de destino?"))
    
if __name__ == '__main__':
    main()