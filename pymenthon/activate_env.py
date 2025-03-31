import os
import sys
import subprocess
def activate_env(env_name):
    env_dir = os.path.join(os.getcwd(), env_name)
    
    if not os.path.exists(env_dir):
        print(f"El entorno {env_name} no existe.")
        return
    
    # Activar entorno en sistemas Linux/MacOS
    activate_script = os.path.join(env_dir, 'bin', 'activate')
    if sys.platform == "win32":
        activate_script = os.path.join(env_dir, 'Scripts', 'activate.bat')
    
    print(f"Activando entorno virtual {env_name}...")
    subprocess.call([activate_script], shell=True)