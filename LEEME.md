# Práctica 02 · CRUD de alumnos modificado

Proyecto completo para mostrar y explicar las modificaciones de la guía del alumno.
Incluye encabezado personalizado, enlaces Inicio/Ayuda, fecha del equipo, campo Turno
al agregar y editar, validaciones y columna Turno en la tabla.

## Abrir y ejecutar en Windows

1. Extrae el ZIP (no trabajes dentro del archivo comprimido).
2. En Visual Studio Code elige Archivo → Abrir carpeta → CRUD_Alumnos_Practica02.
3. Inicia MongoDB Community Server en 127.0.0.1:27017. Compass es opcional;
   tener Compass abierto no sustituye al servidor de MongoDB.
4. Abre Terminal → Nueva terminal. Ejecuta una línea a la vez:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe app.py
```

5. Abre http://127.0.0.1:5000 en el navegador. No uses Live Server.
6. Para detenerlo, presiona Ctrl + C en la terminal.

En sesiones posteriores basta con iniciar MongoDB y ejecutar el último comando.
Se requiere Python 3.11 o posterior compatible. La instalación inicial de paquetes
requiere internet. No se incluyen Python, MongoDB ni un entorno .venv.

## En macOS o Linux

Con Python y MongoDB instalados y el servidor MongoDB iniciado:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python app.py
```

## Datos de la práctica

La base sigue siendo escuela_practica y la colección alumnos. Si la práctica anterior
usaba ese servidor, aparecerán los mismos registros. Copiar el proyecto no copia ni
separa los datos de MongoDB. Usa nombres ficticios y elimina solo tus pruebas.
Los registros antiguos muestran “Sin asignar” hasta que selecciones y guardes su turno.
En un equipo sin registros, la colección se crea al guardar el primer alumno.

## Para explicar en clase

Abre EXPLICACION_DOCENTE.md. En VS Code puedes usar Ctrl + Shift + V para verlo
con formato. Busca NUEVO en app.py para ubicar los cambios comentados.
La guía del alumno se incluye en la carpeta material.

## Comprobación técnica

Se verificaron las rutas y las operaciones con el cliente de pruebas de Flask y
MongoDB simulado. La conexión con el servidor MongoDB real debe comprobarse en el
equipo del laboratorio. El proyecto está configurado para uso local de aprendizaje.
