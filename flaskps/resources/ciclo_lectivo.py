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
from flaskps.models.usuario import User
from flaskps.models.ciclo_lectivo import Ciclo_lectivo
import json, requests

def listadoCiclosLectivos():
    if 'email' not in session or not any(i in ['administrador', 'docente'] for i in session['roles']):
        return redirect(url_for("accesoDenegado"))
    tabla = configuracion.get_config()
    if tabla.sitio_habilitado == 0:
        return redirect(url_for("mantenimiento"))
    lista = Ciclo_lectivo.all()

    return render_template(
        "/ciclo_lectivo/listadoCiclosLectivos.html", lista=lista, cant=tabla.cantListar,
    )

def actualizarCiclosLectivos(id):
    if 'email' not in session or not any(i in ['administrador', 'docente', 'preceptor'] for i in session['roles']):
        return redirect(url_for("accesoDenegado"))
    p = request.form
    Ciclo_lectivo.actualizar(
        id,
        p["fecha_ini"],
        p["fecha_fin"],
        p["semestre"],
    )
    flash('Ciclo lectivo actualizado con exito!')
    return redirect(url_for('listadoCiclosLectivos'))