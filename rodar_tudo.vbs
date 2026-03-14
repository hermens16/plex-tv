Set WshShell = CreateObject("WScript.Shell")

WshShell.CurrentDirectory = "C:\Users\User\Dev\plex-tv"

' inicia servidor
WshShell.Run "cmd /c start py pywsgi.py", 0, False

' espera servidor subir
WScript.Sleep 15000

' gerar playlists
WshShell.Run "py gerar_playlist.py", 0, True

' traduzir
WshShell.Run "py traduzir_playlist.py", 0, True

' organizar
WshShell.Run "py organizar_grupos.py", 0, True

' push git
WshShell.Run "py update_git.py", 0, True