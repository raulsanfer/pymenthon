import subprocess
import sys

def install_dependencies(requirements_file):
    print(f"Instalando dependencias desde {requirements_file}...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", requirements_file])