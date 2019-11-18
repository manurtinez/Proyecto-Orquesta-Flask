from flask import (
    render_template,
    jsonify,
    abort,
    url_for,
    request,
    redirect,
    session,
    flash,
)
from flaskps.models.configuracion import configuracion
from flaskps.models.genero import Genero
from flaskps.models.docente import Docente
import json, requests

def listadoDocentes():
    if 'email' not in session or not any(i in ['administrador', 'docente'] for i in session['roles']):
        return redirect(url_for("accesoDenegado"))
    tabla = configuracion.get_config()
    if tabla.sitio_habilitado == 0:
        return redirect(url_for("mantenimiento"))
    lista = Docente.all()
    tiposDNI = []
    listaLoc = []
    dnis = requests.get(
        "https://api-referencias.proyecto2019.linti.unlp.edu.ar/tipo-documento"
    )
    localidades = requests.get(
        "https://api-referencias.proyecto2019.linti.unlp.edu.ar/localidad"
    )
    dnis = json.loads(dnis.text)
    localidades = json.loads(localidades.text)
    return render_template(
        "/docente/listadoDocentes.html", lista=lista, cant=tabla.cantListar,
        generos=Genero.get_all(),
        dnis=dnis,
        localidades=localidades,
    )
def crearDocente():
    if 'email' not in session or not any(i in ['administrador', 'docente'] for i in session['roles']):
        return redirect(url_for("accesoDenegado"))
    p = request.form
    Docente.create(
        p["apellido"],
        p["nombre"],
        p["fechaN"],
        p["localidad"],
        p["domicilio"],
        p["genero"],
        p["tipoD"],
        p["numero"],
        p["telefono"],
    )
    return redirect(url_for("listadoDocentes"))