# Pymenthon - Gestión de Entornos Virtuales

**Pymenthon** es una librería de Python para crear, activar, desactivar y gestionar entornos virtuales de manera sencilla. Incluye comandos CLI para facilitar el uso.

## Instalación

pip install git+https://github.com/raulsanfer/pymenthon.git

pymenthon create my_project_env --python-version 3.9\
pymenthon activate my_project_env\
pymenthon install --requirements requirements.txt\
pymenthon deactivate\
pymenthon list\


## Consideraciones
Es posible tener varios entornos virtuales de Python activos simultáneamente, pero con algunas consideraciones importantes:

**En diferentes terminales/ventanas de comandos**\
La forma más común y recomendada es tener cada entorno virtual activado en una terminal o ventana de comandos diferente:\

Abre una terminal y activa el entorno virtual A\
Abre otra terminal y activa el entorno virtual B\
Trabaja en ambos entornos simultáneamente

Cada terminal mantendrá su propio contexto de entorno virtual independiente.

**En la misma terminal (con limitaciones)**\
En una misma terminal, cuando activas un entorno virtual, este reemplaza al anterior en tu PATH. 
