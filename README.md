# Spotify To YTMusic 🎵 ➡️ 📺

Este projeto é uma ferramenta em Python desenvolvida para facilitar a migração de músicas entre plataformas de streaming. Atualmente, foca-se em transferir todas as **músicas curtidas (Liked Tracks)** do Spotify para uma nova playlist no YouTube Music.

## ✨ Funcionalidades

* **Autenticação Segura**: Utiliza o fluxo OAuth2 com PKCE para o Spotify e integração via ficheiro de sessão (`browser.json`) para o YouTube Music.
* **Sincronização de Biblioteca**: Obtém automaticamente a lista de todas as músicas que o utilizador marcou com "Gosto" no Spotify.
* **Motor de Busca Inteligente**: Procura as músicas correspondentes no YouTube Music utilizando o título e o nome dos artistas para garantir a melhor precisão.
* **Processamento Paralelo**: Utiliza `joblib` para realizar pesquisas e obter IDs de faixas de forma concorrente, acelerando significativamente o processo.
* **Arquitetura Extensível**: Construído sobre uma classe abstrata `PlayerAPIManager`, permitindo adicionar novos serviços de música facilmente.

## 🛠️ Tecnologias Utilizadas

* **Linguagem**: Python 3.13+
* **APIs e Bibliotecas**: 
    * `requests`: Para interações com a API do Spotify.
    * `ytmusicapi`: Para interagir com o YouTube Music.
    * `Flask`: Para gerir o callback de autenticação do Spotify.
    * `joblib`: Para execução de tarefas em paralelo.

## 🚀 Como Configurar

### 1. Requisitos Prévios
* Ter o Python instalado.
* Criar uma aplicação no [Spotify for Developers](https://developer.spotify.com/) para obter o seu `client_id`.

### 2. Autenticação no YouTube Music
Para que a aplicação aceda à sua conta do YouTube Music, é necessário configurar o ficheiro `browser.json`:
1. Siga as instruções da documentação oficial do `ytmusicapi` para extrair os headers do seu navegador.
2. Guarde os dados no ficheiro `browser.json` na raiz do projeto.

### 3. Instalação
Clone o repositório e instale as dependências:
```bash
pip install requests flask joblib ytmusicapi
