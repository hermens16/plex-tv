
import re

entrada = "playlist.m3u"
saida = "playlist_traduzida.m3u"

traducao = {

    "MOVIES": "FILMES",
    "DRAMA TV": "SÉRIES",
    "KIDS & FAMILY": "INFANTIL",
    "HISTORY & SCIENCE": "DOCUMENTÁRIOS",
    "LIFESTYLE": "VARIEDADES",
    "REALITY": "VARIEDADES",
    "NEWS": "NOTÍCIAS",
    "MUSIC": "MÚSICA",
    "SPORTS": "ESPORTES",
    "ANIME+": "ANIME"

}

with open(entrada, "r", encoding="utf-8") as f:
    conteudo = f.read()

for en, pt in traducao.items():
    conteudo = re.sub(
        f'group-title="{en}"',
        f'group-title="{pt}"',
        conteudo
    )

with open(saida, "w", encoding="utf-8") as f:
    f.write(conteudo)

print("Grupos traduzidos.")
