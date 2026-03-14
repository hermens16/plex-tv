import re
from collections import defaultdict

entrada = "playlist_traduzida.m3u"
saida = "playlist_final.m3u"

grupos = defaultdict(list)

with open(entrada, "r", encoding="utf-8") as f:
    linhas = f.readlines()

for i, linha in enumerate(linhas):

    if linha.startswith("#EXTINF"):

        match = re.search(r'group-title="([^"]+)"', linha)

        if match:
            grupo = match.group(1).upper()
        else:
            grupo = "OUTROS"

        # classificação automática

        if "SPORT" in grupo:
            grupo = "ESPORTES"

        elif "NEWS" in grupo:
            grupo = "NOTÍCIAS"

        elif "MOVIE" in grupo or "FILM" in grupo:
            grupo = "FILMES"

        elif "SERIES" in grupo or "DRAMA" in grupo:
            grupo = "SÉRIES"

        elif "KIDS" in grupo or "FAMILY" in grupo:
            grupo = "INFANTIL"

        elif "MUSIC" in grupo:
            grupo = "MÚSICA"

        elif "DOC" in grupo or "HISTORY" in grupo or "SCIENCE" in grupo:
            grupo = "DOCUMENTÁRIOS"

        elif "ANIME" in grupo:
            grupo = "ANIME"

        elif "LIFESTYLE" in grupo or "REALITY" in grupo:
            grupo = "VARIEDADES"

        stream = linhas[i+1]

        grupos[grupo].append((linha, stream))

with open(saida, "w", encoding="utf-8") as f:

    f.write("#EXTM3U\n")

    ordem = [
        "FILMES",
        "SÉRIES",
        "DOCUMENTÁRIOS",
        "VARIEDADES",
        "INFANTIL",
        "ANIME",
        "ESPORTES",
        "NOTÍCIAS",
        "MÚSICA",
        "INTERNACIONAL",
        "OUTROS"
    ]

    for grupo in ordem:

        if grupo in grupos:

            for canal in grupos[grupo]:

                f.write(canal[0])
                f.write(canal[1])

print("Playlist final criada.")
