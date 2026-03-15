
import re

entrada = "playlist.m3u"
saida = "playlist_final.m3u"

mapa_grupos = {

    "MOVIES": "FILMES",
    "CLASSICS": "FILMES",
    "SCI-FI & ACTION": "FILMES",

    "DRAMA TV": "SÉRIES",
    "SERIES": "SÉRIES",
    "HIT TV": "SÉRIES",

    "HISTORY & SCIENCE": "DOCUMENTÁRIOS",
    "NATURE & TRAVEL": "DOCUMENTÁRIOS",
    "TRUE CRIME": "DOCUMENTÁRIOS",

    "KIDS & FAMILY": "INFANTIL",
    "KIDS": "INFANTIL",

    "LIFESTYLE": "VARIEDADES",
    "REALITY": "VARIEDADES",
    "FOOD & HOME": "VARIEDADES",
    "DAYTIME TV": "VARIEDADES",

    "COMEDY": "VARIEDADES",
    "CHILLS & THRILLS": "FILMES",

    "NEWS": "NOTÍCIAS",

    "MUSIC": "MÚSICA",

    "SPORTS": "ESPORTES",
    "ESPORTES": "ESPORTES",

    "ANIME+": "ANIME",

    "INTERNATIONAL": "INTERNACIONAL",
    "EN ESPAÑOL": "INTERNACIONAL",
}

with open(entrada, "r", encoding="utf-8") as f:
    linhas = f.readlines()

saida_linhas = []

for i in range(len(linhas)):

    linha = linhas[i]

    if linha.startswith("#EXTINF"):

        nome = linha.split(",")[-1].strip().upper()

        grupo = "VARIEDADES"

        if 'group-title="' in linha:
            grupo_original = linha.split('group-title="')[1].split('"')[0].upper()
            grupo = mapa_grupos.get(grupo_original, grupo_original)

        linha = re.sub(r'group-title="[^"]*"', '', linha)

        metadados = linha.split(",")[0]
        metadados = re.sub(r"\s+", " ", metadados).strip()

        nova_linha = f'{metadados} group-title="{grupo}",{nome}\n'

        saida_linhas.append(nova_linha)

    elif linha.startswith("http"):
        saida_linhas.append(linha)

with open(saida, "w", encoding="utf-8") as f:

    f.write("#EXTM3U\n")

    for l in saida_linhas:
        f.write(l)

print("Playlist organizada com sucesso.")
