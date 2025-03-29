from setuptools import setup, find_packages

setup(
    name="pymenthon",            # El nombre del paquete
    version="0.1",               # La versión de tu librería
    packages=find_packages(),    # Encuentra todos los paquetes en el directorio pymenthon/
    install_requires=[           # Dependencias adicionales si las necesitas
        # Puedes agregar aquí las dependencias necesarias como: 'requests', 'flask', etc.
    ],
    entry_points={               # Mapeo de comandos CLI
        "console_scripts": [
            "pymenthon = pymenthon.cli:main",  # Mapea el comando 'pymenthon' al método 'main' en cli.py
        ],
    },
    classifiers=[                # Opcional, para especificar detalles del paquete
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',      # Especifica que se requiere Python 3.6 o superior
)
