arquivos = [
    "plex.m3u",
    "freelivesports_corrigida.m3u"
]

saida = "playlist.m3u"

with open(saida, "w", encoding="utf-8") as outfile:

    outfile.write("#EXTM3U\n")

    for arquivo in arquivos:

        with open(arquivo, "r", encoding="utf-8") as f:

            for linha in f:

                if linha.startswith("#EXTM3U"):
                    continue

                outfile.write(linha)

print("Playlists unidas.")
