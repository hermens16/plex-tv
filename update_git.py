import os

print("Atualizando repositório Git...")

os.system("git add -A")

os.system('git commit -m "Atualização automática da playlist"')

os.system("git branch -M main")

os.system("git push -u origin main --force")

print("Push concluído!")
