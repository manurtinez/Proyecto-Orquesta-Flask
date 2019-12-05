from flask import redirect, render_template, request, session, url_for, flash, jsonify
from flaskps.db import db
from flaskps.models.configuracion import configuracion
from flaskps.models.usuario import User
from flaskps.models.estudiante import Estudiante
from flaskps.models.docente import Docente
from flaskps.resources import user
from flaskps.models.ciclo_lectivo import Ciclo_lectivo
from datetime import datetime

def administracion():
    if 'email' not in session or 'administrador' not in session['roles']:
        return redirect(url_for('accesoDenegado'))
    tabla = configuracion.get_config()
    if tabla.sitio_habilitado == 0:
        return redirect(url_for('mantenimiento'))
    #configuracion.set_titulo("orquesta berisso")
    if request.method == 'POST':
        configuracion.set_titulo(request.form['titulo'])
        configuracion.set_descripcion(request.form['descripcion'])
        configuracion.set_mail(request.form['mail'])
        configuracion.set_cantListar(request.form['cantListar'])
        return redirect(url_for('index'))
    return render_template('/admin/administracion.html', titulo=tabla.titulo, descripcion=tabla.descripcion, mail=tabla.mail, cantListar=tabla.cantListar)

def mantenimiento():  
    return render_template('/admin/desactivar.html', desactivado=True)

def desactivar():
    if 'email' not in session or 'administrador' not in session['roles']:
        return redirect(url_for('accesoDenegado'))
    configuracion.set_habilitacion(0)
    session['sitioActivado'] = False
    return mantenimiento()

def activar():
    if 'email' not in session or 'administrador' not in session['roles']:
        return redirect(url_for('accesoDenegado'))
    configuracion.set_habilitacion(1)
    session['sitioActivado'] = True
    return redirect(url_for('index'))

def eliminarUser(email):
    if 'email' not in session or 'administrador' not in session['roles']:
        return redirect(url_for('accesoDenegado'))
    if session['email'] != email:
        User.eliminar_usuario(email)
        flash('el usuario ha sido eliminado')
        return redirect(url_for('listadoUsers'))
    else:
        flash('no se puede eliminar a usted mismo!')
        return redirect(url_for('listadoUsers'))

def eliminarEstudianteFisico(dni):
    if 'email' not in session or 'administrador' not in session['roles']:
        return redirect(url_for('accesoDenegado'))
    Estudiante.eliminar_estudiante(dni)
    flash('el estudiante ha sido eliminado')
    return redirect(url_for('listadoEstudiantes'))

def reactivarEstudiante():
    if 'email' not in session or 'administrador' not in session['roles']:
        return redirect(url_for('accesoDenegado'))
    id = request.json['id']
    Estudiante.restaurar(id)
    return jsonify({'ok': 'ok'})

def reactivarDocente():
    if 'email' not in session or 'administrador' not in session['roles']:
        return redirect(url_for('accesoDenegado'))
    id = request.json['id']
    Docente.restaurar(id)
    return jsonify({'ok': 'ok'})

def eliminarEstudianteLogico(dni):
    if 'email' not in session or 'administrador' not in session['roles']:
        return redirect(url_for('accesoDenegado'))
    Estudiante.logic_delete(dni)
    flash('el estudiante ha sido eliminado')
    return redirect(url_for('listadoEstudiantes'))

def bloquearUser(id):
    if 'email' not in session or 'administrador' not in session['roles']:
        return redirect(url_for('accesoDenegado'))
    user = User.desactivar_user(User.get_by_id(id).username)
    print(user.activo)
    return redirect(url_for('listadoUsers'))

def activarUser(id):
    if 'email' not in session or 'administrador' not in session['roles']:
        return redirect(url_for('accesoDenegado'))
    user = User.activar_user(User.get_by_id(id).username)
    print(user.activo)
    return redirect(url_for('listadoUsers'))

def accesoDenegado():
    flash('Usted no posee autorizacion para acceder a esta url')
    return redirect(url_for('index'))

def eliminarDocenteFisico(dni):
    if 'email' not in session or 'administrador' not in session['roles']:
        return redirect(url_for('accesoDenegado'))
    Docente.eliminar_docente(dni)
    flash('El docente ha sido eliminado')
    return redirect(url_for('listadoDocentes'))

def eliminarDocenteLogico(dni):
    if 'email' not in session or 'administrador' not in session['roles']:
        return redirect(url_for('accesoDenegado'))
    Docente.logic_delete(dni)
    return redirect(url_for('listadoDocentes'))