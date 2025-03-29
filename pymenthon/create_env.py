import os
import subprocess
import sys
import venv

def create_env(env_name, python_version="3.9"):
    env_dir = os.path.join(os.getcwd(), env_name)
    
    if os.path.exists(env_dir):
        print(f"El entorno {env_name} ya existe.")
        return
    
    # Crea el entorno virtual con el python especificado
    python_path = f"python{python_version}"
    print(f"Creando entorno virtual con Python {python_version}...")
    venv.create(env_dir, with_pip=True)
    
    print(f"Entorno {env_name} creado en {env_dir}.")
    return env_dir