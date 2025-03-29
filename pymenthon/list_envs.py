import os

def list_envs():
    print("Entornos virtuales existentes:")
    for item in os.listdir(os.getcwd()):
        if os.path.isdir(item) and "env" in item:
            print(f"- {item}")