from flask import render_template, abort, url_for, request, redirect, session, flash
from flaskps.models.usuario import User
from flaskps.models.usuario_tiene_rol import User_tiene_rol
from flaskps.models.rol import Rol
from datetime import date
from flaskps.models.configuracion import configuracion
from flaskps.resources import admin

def registrar():
    tabla = configuracion.get_config()
    if tabla.sitio_habilitado == 0:
        return redirect(url_for('mantenimiento'))
    return render_template('user/registro.html')

def crear():
    if 'email' not in session or 'administrador' not in session['roles']:
        return redirect(url_for('accesoDenegado'))
    p = request.form
    user = User.get_by_email(p['email'])
    if user:
        flash('el mail ya se encuentra registrado!')
        return redirect(url_for('registro'))
    else:
        User.create(p['email'], p['user'], p['password'], 1, p['nombre'], p['apellido'])
        return redirect(url_for('index'))

def listadoUsers():
    if 'email' not in session or 'administrador' not in session['roles']:
        return redirect(url_for('accesoDenegado'))
    tabla = configuracion.get_config()
    if tabla.sitio_habilitado == 0:
        return redirect(url_for('mantenimiento'))
    lista = User.all()
    roles = Rol.all()
    rolesUsers = {}
    for user in lista:
        aux = []
        for rol in roles:
            if User_tiene_rol.tiene_rol(user.id, rol.id):
                aux.append(rol)
        rolesUsers[user.id] = aux
    return render_template('user/listadoUsers.html', lista=lista, cant=tabla.cantListar, roles=roles, rolesUsers=rolesUsers)

def actualizar(m):
    if 'email' not in session or 'administrador' not in session['roles']:
        return redirect(url_for("accesoDenegado"))
    p = request.form
    act = User.get_by_email(m)
    roles = Rol.all()
    User.actualizar(act.username, p['username'],p['password'], p['nombre'], p['apellido'])
    for r in roles:
        c = 'rol' + str(r.id)
        if request.form.get(c):
            User_tiene_rol.asignar_rol(act.id, r.id)
        else:
            User_tiene_rol.desasignar_rol(act.id, r.id)
    return redirect(url_for('listadoUsers'))

def mostrarActivos():
    if 'email' not in session or 'administrador' not in session['roles']:
        return redirect(url_for("accesoDenegado"))
    lista = User.select_activos()
    tabla = configuracion.get_config()
    return render_template('user/listado.html', lista=lista, cant=tabla.cantListar)

def mostrarInactivos():
    if 'email' not in session or 'administrador' not in session['roles']:
        return redirect(url_for("accesoDenegado"))
    lista = User.select_inactivos()
    tabla = configuracion.get_config()
    return render_template('user/listado.html', lista=lista, cant=tabla.cantListar)