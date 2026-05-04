from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

# Importando suas classes (ajuste o caminho se necessário)
from managers.SpotifyAPIManager import SpotifyAPIManager
from managers.YTmusicAPIManager import YTmusicAPIManager
from managers.TransferClass import TransferClass

app = FastAPI(title="MoveMusic API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 1. Instanciamos os gerenciadores "globalmente" para guardar o estado da sessão
spotify_manager = SpotifyAPIManager()
yt_manager = YTmusicAPIManager()
transfer_manager = TransferClass(origin=spotify_manager, destine=yt_manager)


@app.get("/api/spotify/auth-url")
def get_spotify_url():
    """ Rota que o Flutter vai chamar para pegar o link de login """
    url = spotify_manager.get_authorization_url()
    return {"url": url}


@app.get("/callback")
def spotify_callback(code: str):
    """ O Spotify vai jogar o usuário de volta aqui com o código secreto """
    spotify_manager.set_auth_code(code)
    
    # Retornamos um HTML bonitinho para o usuário saber que deu certo
    html_content = """
    <html>
        <body style="display:flex; justify-content:center; align-items:center; height:100vh; font-family:sans-serif; background-color:#1db954; color:white;">
            <div style="text-align:center;">
                <h1>Autorização Concluída! 🎵</h1>
                <p>O back-end já está conectado. Você pode fechar esta aba e voltar para o aplicativo.</p>
            </div>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)


@app.post("/api/transferir")
def iniciar_transferencia(playlist_destino: str):
    """ Rota para disparar a transferência. Como não usamos 'async def', 
        o FastAPI roda isso numa thread separada magicamente. """
    
    if not spotify_manager.auth_code:
        return {"status": "erro", "mensagem": "Usuário não autenticado no Spotify."}
    
    # Dispara sua lógica original!
    transfer_manager.transfer_liked_tracks(playlist_destino)
    
    return {"status": "sucesso", "mensagem": f"Transferência para '{playlist_destino}' concluída!"}


# import backend.SpotifyAPIManager as sAPI
# import backend.YTmusicAPIManager as ytAPI
# import backend.TransferClass as tAPI

# def main():
#     ytConn = ytAPI.YTmusicAPIManager()
#     sConn  = sAPI.SpotifyAPIManager()

#     tranferConn = tAPI.TransferClass(ytConn, sConn)
#     tranferConn.transfer_liked_tracks(input("Qual o nome da playlist de destino?"))
    
# if __name__ == '__main__':
#     main()