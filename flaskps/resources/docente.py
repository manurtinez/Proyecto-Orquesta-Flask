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
from flaskps.models.usuario import User
import json, requests

def listadoDocentes():
    if 'email' not in session or not any(i in ['administrador', 'docente'] for i in session['roles']):
        return redirect(url_for("accesoDenegado"))
    tabla = configuracion.get_config()
    if tabla.sitio_habilitado == 0:
        return redirect(url_for("mantenimiento"))
    lista = Docente.notDeletedAll()
    eliminados = Docente.deletedAll()
    try:
        dnis = requests.get(
            "https://api-referencias.proyecto2019.linti.unlp.edu.ar/tipo-documento"
        )
        localidades = requests.get(
            "https://api-referencias.proyecto2019.linti.unlp.edu.ar/localidad"
        )
        tiposDNI = json.loads(dnis.text)
        listaLoc = json.loads(localidades.text)
    except requests.exceptions.ConnectionError:
        flash('hubo un error al traer datos de los dnis y/o localidades :(')
        return redirect(url_for('index'))
    return render_template(
        "/docente/listadoDocentes.html", lista=lista, cant=tabla.cantListar,
        generos=Genero.get_all(),
        dnis=tiposDNI,
        localidades=listaLoc,
        eliminados=eliminados,
    )
def crearDocente():
    if 'email' not in session or not any(i in ['administrador', 'docente'] for i in session['roles']):
        return redirect(url_for("accesoDenegado"))
    p = request.form
    if Docente.getByDNI(p['numero']) is not None:
        flash('ya existe un docente con ese numero de documento!')
        return redirect(url_for('listadoDocentes'))
    else:
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

def actualizarDocente(dni):
    if 'email' not in session or not any(i in ['administrador', 'docente', 'preceptor'] for i in session['roles']):
        return redirect(url_for("accesoDenegado"))
    p = request.form
    Docente.actualizar(
        dni,
        p["apellido"],
        p["nombre"],
        p["fechaN"],
        p["localidad"],
        p["domicilio"],
        p["genero"],
        p["tipoD"],
        p["telefono"],
    )
    flash('docente actualizado con exito!')
    return redirect(url_for('listadoDocentes'))