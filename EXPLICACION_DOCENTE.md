# Recorrido para explicar las modificaciones

Abre primero la aplicación en el navegador y después muestra el código en VS Code.
Puedes alternar entre ambos para que el grupo relacione cada cambio con su resultado.

## 1. Mostrar qué cambió

Señala el encabezado, el enlace Ayuda y la lista Turno. Explica:
“Trabajamos sobre el mismo registro. Ahora vamos a reconocer en qué archivo vive
cada parte y cómo se conectan cuando guardamos un alumno”.

## 2. Ubicar los archivos

| Archivo | Qué mostrar |
|---|---|
| app.py | Herramientas, conexión, lectura de datos y rutas. |
| requirements.txt | Flask y PyMongo son los paquetes que instalamos. |
| templates/base.html | Encabezado compartido y enlaces Inicio/Ayuda. |
| templates/ayuda.html | Nueva pantalla que recibe la fecha. |
| templates/index.html | Formulario de registro y columna Turno. |
| templates/editar.html | Formulario con el turno actual seleccionado. |
| static/estilos.css | Apariencia de la aplicación. |

## 3. Explicar la nueva herramienta

Busca `from datetime import datetime` en app.py.
“Importar es traer una herramienta para utilizarla en este archivo. datetime ya viene
con Python. Por eso no tuvimos que instalarla ni escribirla en requirements.txt”.

## 4. Recorrer la nueva ruta

Busca `@app.route("/ayuda")`.

- `/ayuda` es la dirección que se solicita en el navegador.
- `def ayuda():` es la función que atiende esa dirección.
- `datetime.now()` obtiene la fecha y hora del equipo que ejecuta Python.
- `strftime("%d/%m/%Y")` muestra día, mes y año.
- `render_template("ayuda.html", fecha=fecha)` abre la plantilla y le pasa la fecha.

Abre ayuda.html y señala `{{ fecha }}`: “Aquí se muestra el valor que envió Python”.
Después abre base.html y señala `url_for('ayuda')`: usa el nombre de la función,
no el nombre del archivo. Haz clic en Ayuda en el navegador para cerrar el recorrido.

## 5. Seguir el turno desde el formulario hasta MongoDB

1. En index.html, busca `name="turno"`. Es el nombre con el que viaja el dato.
2. En app.py, busca `request.form.get("turno", "")`. Python recoge ese mismo nombre.
3. Señala `strip()`: elimina espacios sobrantes al principio y al final.
4. Señala la validación: se aceptan Matutino y Vespertino; no se permite dejarlo vacío.
5. Señala el `return` de leer_formulario: ahora entrega nombre, grupo y turno.
6. En agregar, señala `datos = leer_formulario()` e `insert_one(datos)`.
   No se necesitó una instrucción de guardado separada para turno.
7. En index.html, busca `alumno.get('turno', 'Sin asignar')`: muestra el dato guardado.
   “Sin asignar” es un texto de presentación; no modifica automáticamente la base.

Registra: Ana Prueba / 501 / Matutino. Actualiza el navegador y comprueba que permanece.

## 6. Mostrar cómo se edita

Abre editar.html y busca `selected`. Esa parte deja marcado el turno actual.
En app.py, editar vuelve a llamar a leer_formulario y actualiza con `$set`.
Cambia a Ana Prueba de Matutino a Vespertino y guarda. Comprueba la tabla.
Si un alumno antiguo no tiene turno, se le pide elegirlo al guardar su edición.

## 7. Comprobar y cerrar

- Intenta guardar sin turno: el navegador pide completar la selección.
- Explica que Python también valida el dato, aunque se evite la revisión del navegador.
- Abre Ayuda y vuelve a Inicio.
- Elimina solamente a Ana Prueba, después de confirmar.

Preguntas para el grupo:
1. ¿En qué archivo cambiarían el título visible?
2. ¿Qué diferencia hay entre la ruta /ayuda y el archivo templates/ayuda.html?
3. ¿Por qué name="turno" debe coincidir con el nombre que lee Python?
4. ¿Qué faltaría si agregáramos un dato al registro, pero no a la pantalla de edición?

## Si aparece un error

Si no abre la aplicación, revisa primero la terminal y que no haya otra práctica usando
el puerto 5000. Detén esa ejecución antes de iniciar esta. Si aparece el mensaje de
MongoDB, comprueba que su servicio esté iniciado. Si falta un paquete, repite la
instalación de requirements.txt con el Python de .venv indicado en LEEME.md.
