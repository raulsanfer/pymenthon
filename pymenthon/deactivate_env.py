import sys

def deactivate_env():
    print("Desactivando entorno virtual...")
    if sys.platform == "win32":
        subprocess.call("deactivate", shell=True)
    else:
        print("En sistemas Unix se desactiva con el comando 'deactivate'.")