Set WshShell = CreateObject("WScript.Shell")

WshShell.CurrentDirectory = "C:\Users\User\Dev\plex-tv"

' inicia o servidor em background
WshShell.Run "py pywsgi.py", 0, False

' espera o servidor iniciar
WScript.Sleep 15000

' gera playlists
WshShell.Run "py gerar_playlist.py", 0, True

' corrige lista de esportes
WshShell.Run "py corrigir_sports.py", 0, True

' junta plex + freelivesports
WshShell.Run "py juntar_playlists.py", 0, True

' organiza, traduz e padroniza tudo
WshShell.Run "py organizar_playlist_final.py", 0, True

' faz commit e push
WshShell.Run "py update_git.py", 0, True