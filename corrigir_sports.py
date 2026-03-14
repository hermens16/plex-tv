import re

entrada = "freelivesports.m3u"
saida = "freelivesports_corrigida.m3u"

with open(entrada, "r", encoding="utf-8") as f:
    linhas = f.readlines()

saida_linhas = []

for linha in linhas:

    if linha.startswith("#EXTINF"):

        # remove qualquer group-title existente
        linha = re.sub(r'group-title="[^"]*"', '', linha)

        # adiciona ESPORTES
        linha = linha.replace(
            "#EXTINF:-1",
            '#EXTINF:-1 group-title="ESPORTES"'
        )

    saida_linhas.append(linha)

with open(saida, "w", encoding="utf-8") as f:
    f.writelines(saida_linhas)

print("Todos os canais da FreeliveSports agora são ESPORTES.")
