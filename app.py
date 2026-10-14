# HERRAMIENTAS: se importan al inicio del archivo.
from flask import Flask, render_template, request, redirect, url_for, abort
from pymongo import MongoClient
from pymongo.errors import PyMongoError
from bson import ObjectId
# NUEVO: datetime viene con Python; no requiere instalar otro paquete.
from datetime import datetime

# CONEXIÓN: se mantiene la misma base de la práctica anterior.
app = Flask(__name__)
cliente = MongoClient("mongodb://127.0.0.1:27017/", serverSelectionTimeoutMS=3000)
base_datos = cliente["escuela_practica"]
alumnos = base_datos["alumnos"]

# FORMULARIO: esta función se usa tanto al agregar como al editar.
def leer_formulario():
    nombre = request.form.get("nombre", "").strip()
    grupo = request.form.get("grupo", "").strip()
    # NUEVO: "turno" coincide con name="turno" en los dos formularios HTML.
    turno = request.form.get("turno", "").strip()
    if not nombre or not grupo or not turno:
        abort(400, description="Completa nombre, grupo y turno.")
    if len(nombre) > 80 or len(grupo) > 20:
        abort(400, description="Usa hasta 80 caracteres en nombre y 20 en grupo.")
    # NUEVO: solo aceptamos las dos opciones previstas.
    if turno not in ["Matutino", "Vespertino"]:
        abort(400, description="Selecciona un turno válido.")
    # NUEVO: el turno viaja junto con nombre y grupo para guardarse.
    return {"nombre": nombre, "grupo": grupo, "turno": turno}

# BUSCAR: comprueba la clave y recupera el alumno seleccionado.
def buscar_alumno(id):
    if not ObjectId.is_valid(id):
        abort(404, description="La clave del alumno no es válida.")
    alumno = alumnos.find_one({"_id": ObjectId(id)})
    if alumno is None:
        abort(404, description="Este alumno ya no existe.")
    return alumno

# RUTA INICIO: consulta los registros y carga la pantalla principal.
@app.route("/")
def inicio():
    lista = list(alumnos.find().sort("nombre", 1))
    return render_template("index.html", alumnos=lista)

# RUTA AGREGAR: recibe los tres datos y crea el registro.
@app.route("/agregar", methods=["POST"])
def agregar():
    datos = leer_formulario()
    alumnos.insert_one(datos)
    return redirect(url_for("inicio"))

# RUTA EDITAR: GET muestra el formulario y POST guarda los cambios.
@app.route("/editar/<id>", methods=["GET", "POST"])
def editar(id):
    alumno = buscar_alumno(id)
    if request.method == "POST":
        datos = leer_formulario()
        alumnos.update_one({"_id": alumno["_id"]}, {"$set": datos})
        return redirect(url_for("inicio"))
    return render_template("editar.html", alumno=alumno)

# RUTA ELIMINAR: borra solamente el registro con la clave recibida.
@app.route("/eliminar/<id>", methods=["POST"])
def eliminar(id):
    alumno = buscar_alumno(id)
    alumnos.delete_one({"_id": alumno["_id"]})
    return redirect(url_for("inicio"))

# ERRORES: muestra una explicación cuando la base no está disponible.
@app.errorhandler(PyMongoError)
def error_mongo(error):
    return render_template("error.html", mensaje="No fue posible trabajar con MongoDB. Revisa que el servicio esté iniciado y vuelve a intentar."), 503

@app.errorhandler(400)
@app.errorhandler(404)
def error_peticion(error):
    return render_template("error.html", mensaje=error.description), error.code

# NUEVO: esta ruta carga ayuda.html y le entrega la fecha del equipo.
@app.route("/ayuda")
def ayuda():
    fecha = datetime.now().strftime("%d/%m/%Y")
    return render_template("ayuda.html", fecha=fecha)

# ARRANQUE LOCAL: las rutas deben estar antes de este bloque.
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
