import re

entrada = "freelivesports.m3u"
saida = "freelivesports_corrigida.m3u"

with open(entrada, "r", encoding="utf-8") as f:
    linhas = f.readlines()

saida_linhas = []

for linha in linhas:

    if linha.startswith("#EXTINF"):

        # separa metadados do nome do canal
        partes = linha.split(",", 1)

        metadados = partes[0]
        nome = partes[1]

        # remove qualquer group-title existente
        metadados = re.sub(r'group-title="[^"]*"', '', metadados)

        # limpa espaços duplicados
        metadados = re.sub(r'\s+', ' ', metadados).strip()

        # adiciona group-title no final
        metadados = metadados + ' group-title="ESPORTES"'

        linha = metadados + "," + nome

    saida_linhas.append(linha)

with open(saida, "w", encoding="utf-8") as f:
    f.writelines(saida_linhas)

print("FreeliveSports corrigida com group-title no final.")
