import re
from collections import defaultdict

entrada = "playlist_traduzida.m3u"
saida = "playlist_final.m3u"

mapa = {

"CLÁSSICOS":"FILMES",
"FILMES":"FILMES",
"FICÇÃO & AÇÃO":"FILMES",
"TERROR & SUSPENSE":"FILMES",

"DRAMA":"SÉRIES",
"SÉRIES":"SÉRIES",

"NATUREZA & VIAGEM":"DOCUMENTÁRIOS",
"HISTÓRIA & CIÊNCIA":"DOCUMENTÁRIOS",
"CRIME REAL":"DOCUMENTÁRIOS",

"ESTILO DE VIDA":"VARIEDADES",
"CULINÁRIA & CASA":"VARIEDADES",
"PROGRAMAS DIURNOS":"VARIEDADES",
"REALITY":"VARIEDADES",

"INFANTIL":"INFANTIL",
"ANIME":"ANIME",

"MÚSICA":"MÚSICA",
"NOTÍCIAS":"NOTÍCIAS",
"ESPORTES":"ESPORTES",
"INTERNACIONAL":"INTERNACIONAL"

}

grupos = defaultdict(list)

with open(entrada,"r",encoding="utf-8") as f:
    linhas = f.readlines()

for i,linha in enumerate(linhas):

    if linha.startswith("#EXTINF"):

        match = re.search(r'group-title="([^"]+)"',linha)

        if match:

            grupo = match.group(1)

            if grupo in mapa:

                novo_grupo = mapa[grupo]

                linha = linha.replace(grupo,novo_grupo)

                stream = linhas[i+1]

                grupos[novo_grupo].append((linha,stream))

with open(saida,"w",encoding="utf-8") as f:

    f.write("#EXTM3U\n")

    for grupo in sorted(grupos):

        for canal in grupos[grupo]:

            f.write(canal[0])
            f.write(canal[1])

print("Playlist final criada")
