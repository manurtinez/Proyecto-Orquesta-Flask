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
from datetime import datetime

def listadoCiclosLectivos():
    tabla = configuracion.get_config()
    if tabla.sitio_habilitado == 0:
        return redirect(url_for("mantenimiento"))
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
    tabla = configuracion.get_config()
    if tabla.sitio_habilitado == 0:
        return redirect(url_for("mantenimiento"))
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

def crearciclolectivo():
    tabla = configuracion.get_config()
    if tabla.sitio_habilitado == 0:
        return redirect(url_for("mantenimiento"))
    if 'email' not in session or 'administrador' not in session['roles']:
        return redirect(url_for('accesoDenegado'))
    p = request.form
    inicio = datetime.strptime(p['inicio'], '%Y-%m-%d')
    fin = datetime.strptime(p['fin'], '%Y-%m-%d')
    sem = int(request.form['semestre'])
    if not Ciclo_lectivo.get(inicio, fin, sem):
        aux = Ciclo_lectivo.getByYear(inicio.year)
        if (inicio > fin):
            return jsonify({'ok':'fechainimayor'})
        else:
            for a in aux:
                if a.semestre == sem:
                    return jsonify({'ok': 'semrep'})
            Ciclo_lectivo.create(inicio, fin,sem)
            flash('El ciclo lectivo se generó exitosamente')
            return jsonify({'ok': 'ok'})
    else:
        return jsonify({'ok': 'existe'})

def eliminarCicloLectivo(id):
    tabla = configuracion.get_config()
    if tabla.sitio_habilitado == 0:
        return redirect(url_for("mantenimiento"))
    if 'email' not in session or 'administrador' not in session['roles']:
        return redirect(url_for('accesoDenegado'))
    Ciclo_lectivo.eliminar_ciclolectivo(id)
    flash('El ciclo lectivo ha sido eliminado')
    return redirect(url_for('listadoCiclosLectivos'))