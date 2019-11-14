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
    p = request.form
    user = User.get_by_email(p['email'])
    if user:
        flash('el mail ya se encuentra registrado!')
        return redirect(url_for('registro'))
    else:
        User.create(p['email'], p['user'], p['password'], 1, p['nombre'], p['apellido'])
        usuario = User.get_by_email_and_pass(p['email'], p['password'])
        session['email'] = usuario.email
        session['admin'] = verificarSiEsAdmin()
        return redirect(url_for('index'))

def listadoUsers():
    if 'username' not in session:
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
    print(rolesUsers)
    return render_template('user/listado.html', lista=lista, cant=tabla.cantListar, roles=roles, rolesUsers=rolesUsers)

def verificarSiEsAdmin():
    u = User_tiene_rol.tiene_rol(User.get_by_email(session['email']).id, Rol.get_by_nombre('administrador').id)
    if u !=None:
        return True
    else:
        return False

def showUser(id):
    if 'username' not in session:
        return redirect(url_for('accesoDenegado'))
    print(id)
    return render_template('/user/showUser.html', usuario=id)

def actualizar(m):
    p = request.form
    print(p)
    act = User.get_by_email(m)
    roles = Rol.all()
    print(act)
    User.actualizar(act.username, p['username'],p['password'], p['nombre'], p['apellido'])
    for r in roles:
        c = 'rol' + str(r.id)
        if request.form.get(c):
            User_tiene_rol.asignar_rol(act.id, r.id)
        else:
            User_tiene_rol.desasignar_rol(act.id, r.id)
    return redirect(url_for('listadoUsers'))

def buscar():
    if 'username' not in session:
        return redirect(url_for('accesoDenegado'))
    nombre = request.form['nombre']
    user = User.get_by_username(nombre)
    if nombre == '' or not user:
        lista = User.all()
    else:
        lista = []
        for u in user:
            lista.append(u)
    return render_template('user/listado.html', lista=lista)

def mostrarActivos():
    lista = User.select_activos()
    tabla = configuracion.get_config()
    return render_template('user/listado.html', lista=lista, cant=tabla.cantListar)

def mostrarInactivos():
    lista = User.select_inactivos()
    tabla = configuracion.get_config()
    return render_template('user/listado.html', lista=lista, cant=tabla.cantListar)