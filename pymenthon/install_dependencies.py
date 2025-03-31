import subprocess
import sys

def install_dependencies(requirements_path):
    print(f"Instalando dependencias desde {requirements_path}...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", requirements_path])