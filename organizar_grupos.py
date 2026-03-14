entrada = "playlist.m3u"
saida = "playlist_final.m3u"

grupos = {}

with open(entrada, "r", encoding="utf-8") as f:
    linhas = f.readlines()

for i in range(len(linhas)):

    linha = linhas[i]

    if linha.startswith("#EXTINF"):

        grupo = "OUTROS"

        if 'group-title="' in linha:
            grupo = linha.split('group-title="')[1].split('"')[0]

        canal = linha
        url = linhas[i+1]

        if grupo not in grupos:
            grupos[grupo] = []

        grupos[grupo].append((canal, url))

with open(saida, "w", encoding="utf-8") as f:

    f.write("#EXTM3U\n")

    for grupo in sorted(grupos):

        for canal, url in grupos[grupo]:

            f.write(canal)
            f.write(url)

print("Playlist organizada.")
