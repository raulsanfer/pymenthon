import argparse
from pymenthon.create_env import create_env
from pymenthon.activate_env import activate_env
from pymenthon.install_dependencies import install_dependencies
from pymenthon.deactivate_env import deactivate_env
from pymenthon.list_envs import list_envs

def main():
    parser = argparse.ArgumentParser(description="Pymenthon - Gestión de entornos virtuales.")
    subparsers = parser.add_subparsers()

    # Comando para crear entorno
    create_parser = subparsers.add_parser('create', help='Crear un entorno virtual')
    create_parser.add_argument('env_name', type=str, help='Nombre del entorno')
    create_parser.add_argument('--python', type=str, default='3.9', help='Versión de Python')
    create_parser.set_defaults(func=create_env)

    # Comando para activar entorno
    activate_parser = subparsers.add_parser('activate', help='Activar un entorno virtual')
    activate_parser.add_argument('env_name', type=str, help='Nombre del entorno')
    activate_parser.set_defaults(func=activate_env)

    # Comando para instalar dependencias
    install_parser = subparsers.add_parser('install', help='Instalar dependencias desde un archivo requirements.txt')
    install_parser.add_argument('--requirements', type=str, required=True, help='Ruta al archivo requirements.txt')
    install_parser.set_defaults(func=install_dependencies)

    # Comando para desactivar entorno
    deactivate_parser = subparsers.add_parser('deactivate', help='Desactivar el entorno virtual')
    deactivate_parser.set_defaults(func=deactivate_env)

    # Comando para listar entornos
    list_parser = subparsers.add_parser('list', help='Listar los entornos virtuales creados')
    list_parser.set_defaults(func=list_envs)

    args = parser.parse_args()
    args.func(**vars(args))

if __name__ == '__main__':
    main()