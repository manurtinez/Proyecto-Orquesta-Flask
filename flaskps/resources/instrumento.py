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
from flaskps.models.instrumento import Instrumento
import json, requests
from datetime import datetime
from flaskps.models.tipo_instrumento import Tipo_instrumento

def listadoInstrumentos():
    tabla = configuracion.get_config()
    if tabla.sitio_habilitado == 0:
        return redirect(url_for("mantenimiento"))
    if 'email' not in session or not any(i in ['administrador', 'docente'] for i in session['roles']):
        return redirect(url_for("accesoDenegado"))
    tabla = configuracion.get_config()
    if tabla.sitio_habilitado == 0:
        return redirect(url_for("mantenimiento"))
    lista = Instrumento.notDeletedAll()
    eliminados = Instrumento.deletedAll()
    return render_template(
        "/instrumento/listadoInstrumentos.html", lista=lista, eliminados=eliminados, cant=tabla.cantListar, tiposins=Tipo_instrumento.all()
    )

def actualizarInstrumentos(id):
    tabla = configuracion.get_config()
    if tabla.sitio_habilitado == 0:
        return redirect(url_for("mantenimiento"))
    if 'email' not in session or not any(i in ['administrador', 'docente', 'preceptor'] for i in session['roles']):
        return redirect(url_for("accesoDenegado"))
    p = request.form
    Instrumento.actualizar(
        id,
        p["nombre"],
        p["tipoins"],
        p["numero_inventario"],
        p["foto"]
    )
    flash('Instrumento actualizado con exito!')
    return redirect(url_for('listadoInstrumentos'))

def crearInstrumento():
    tabla = configuracion.get_config()
    if tabla.sitio_habilitado == 0:
        return redirect(url_for("mantenimiento"))
    if 'email' not in session or 'administrador' not in session['roles']:
        return redirect(url_for('accesoDenegado'))
    p = request.form
    nombre = p["nombre"]
    tipo_id = int(p['tipo_id'])
    numero_inventario = int(p["numero_inventario"])
    foto = p["foto"]
    Instrumento.create(nombre, tipo_id, numero_inventario, foto)
    flash('El instrumento generó exitosamente')
    return redirect(url_for('listadoInstrumentos'))

def eliminarInstrumento(id):
    tabla = configuracion.get_config()
    if tabla.sitio_habilitado == 0:
        return redirect(url_for("mantenimiento"))
    if 'email' not in session or 'administrador' not in session['roles']:
        return redirect(url_for('accesoDenegado'))
    Instrumento.logic_delete(id)
    flash('El instrumento ha sido eliminado')
    return redirect(url_for('listadoInstrumentos'))