import re

entrada = "freelivesports.m3u"
saida = "freelivesports_corrigida.m3u"

with open(entrada, "r", encoding="utf-8") as f:
    linhas = f.readlines()

saida_linhas = []

for linha in linhas:

    if linha.startswith("#EXTINF"):

        if "group-title" not in linha:
            linha = linha.replace("#EXTINF:-1", '#EXTINF:-1 group-title="ESPORTES"')

    saida_linhas.append(linha)

with open(saida, "w", encoding="utf-8") as f:
    f.writelines(saida_linhas)

print("Lista de esportes corrigida.")
