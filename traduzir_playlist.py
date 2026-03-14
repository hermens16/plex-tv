import re

entrada = "playlist.m3u"
saida = "playlist_traduzida.m3u"

traducao = {

"NEWS": "NOTÍCIAS",
"LIFESTYLE": "ESTILO DE VIDA",
"CLASSICS": "CLÁSSICOS",
"SPORTS": "ESPORTES",
"SCI-FI & ACTION": "FICÇÃO & AÇÃO",
"FOOD & HOME": "CULINÁRIA & CASA",
"KIDS & FAMILY": "INFANTIL",
"INTERNATIONAL": "INTERNACIONAL",
"MUSIC": "MÚSICA",
"COMEDY": "COMÉDIA",
"DAYTIME TV": "PROGRAMAS DIURNOS",
"TRUE CRIME": "CRIME REAL",
"MOVIES": "FILMES",
"REALITY": "REALITY",
"NATURE & TRAVEL": "NATUREZA & VIAGEM",
"HISTORY & SCIENCE": "HISTÓRIA & CIÊNCIA",
"ANIME+": "ANIME",
"DRAMA TV": "DRAMA",
"HIT TV": "SÉRIES",
"CHILLS & THRILLS": "TERROR & SUSPENSE",
"EN ESPAÑOL": "ESPANHOL"

}

with open(entrada, "r", encoding="utf-8", errors="ignore") as f:
    linhas = f.readlines()

saida_linhas = []

for linha in linhas:

    if "group-title" in linha:

        match = re.search(r'group-title="([^"]+)"', linha)

        if match:

            grupo = match.group(1)

            grupo = grupo.replace("EN ESPA├æOL","EN ESPAÑOL")

            if grupo in traducao:
                grupo = traducao[grupo]

            grupo = grupo.upper()

            linha = re.sub(r'group-title="[^"]+"', f'group-title="{grupo}"', linha)

        partes = linha.split(",")

        if len(partes) > 1:

            canal = partes[-1].strip().upper()

            linha = ",".join(partes[:-1]) + "," + canal + "\n"

    saida_linhas.append(linha)

with open(saida, "w", encoding="utf-8") as f:
    f.writelines(saida_linhas)

print("Playlist traduzida criada")
