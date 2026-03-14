Set WshShell = CreateObject("WScript.Shell")

WshShell.CurrentDirectory = "C:\Users\User\Dev\plex-tv"

WshShell.Run "py gerar_playlist.py", 0, True
WshShell.Run "py traduzir_playlist.py", 0, True
WshShell.Run "py organizar_grupos.py", 0, True
WshShell.Run "py update_git.py", 0, True