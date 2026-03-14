import requests
import time
import re

urls = [
    "http://localhost:7777/plex/playlist.m3u",
    "http://localhost:7777/freelivesports/playlist.m3u"
]

files = []

print("Aguardando servidor...")

for i in range(30):
    try:
        r = requests.get(urls[0], timeout=10)
        if r.status_code == 200:
            print("Servidor pronto!")
            break
    except:
        pass
    time.sleep(2)

print("Baixando playlists...")

for url in urls:
    name = url.split("/")[-2] + ".m3u"

    r = requests.get(url, timeout=120)

    with open(name, "wb") as f:
        f.write(r.content)

    files.append(name)

print("Juntando playlists...")

conteudo = ""

for f in files:
    with open(f, "r", encoding="utf-8", errors="ignore") as inp:
        conteudo += inp.read()

linhas = conteudo.splitlines()

# Tradução de grupos
traducoes = {
    "CLASSIC": "CLÁSSICO",
    "KIDS & FAMILY": "KIDS & FAMÍLIA",
    "COMEDY": "COMÉDIA",
    "NEWS": "NOTÍCIAS",
    "SPORTS": "ESPORTES",
    "MOVIES": "FILMES",
    "ENTERTAINMENT": "ENTRETENIMENTO",
    "DOCUMENTARY": "DOCUMENTÁRIOS",
    "LIFESTYLE": "ESTILO DE VIDA",
    "REALITY": "REALITY",
    "MUSIC": "MÚSICA"
}

nova_playlist = []

for linha in linhas:

    if linha.startswith("#EXTINF"):

        # traduz grupos
        for en, pt in traducoes.items():
            linha = linha.replace(en, pt)

        # coloca grupo em maiúsculo
        match = re.search(r'group-title="([^"]+)"', linha)
        if match:
            grupo = match.group(1).upper()
            linha = linha.replace(match.group(1), grupo)

        # coloca nome do canal em maiúsculo
        if "," in linha:
            parte1, parte2 = linha.split(",", 1)
            linha = parte1 + "," + parte2.upper()

    nova_playlist.append(linha)

print("Criando playlist organizada...")

with open("playlist.m3u", "w", encoding="utf-8") as out:
    out.write("\n".join(nova_playlist))

print("Playlist final criada com sucesso!")
