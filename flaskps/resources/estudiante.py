from flask import render_template, abort, url_for, request, redirect, session, flash
from flaskps.models import configuracion
from flaskps.models.usuario import User


def listadoEstudiantes():
    if 'username' not in session:
        return redirect(url_for('accesoDenegado'))
    tabla = configuracion.get_config()
    if tabla.sitio_habilitado == 0:
        return redirect(url_for('mantenimiento'))
    lista = User.all()
    return render_template('user/listado.html', lista=lista, cant=tabla.cantListar)