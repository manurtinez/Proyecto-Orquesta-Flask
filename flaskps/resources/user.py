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
    if session['username'] != None:
        #User.create() esto falta
        return redirect(url_for('index'))
    else:
        p = request.form
        user = User.get_by_email(p['email'])
        if user:
            flash('el mail ya se encuentra registrado!')
            return redirect(url_for('registro'))
        else:
            User.create(p['email'], p['user'], p['password'], 1, date.today(), date.today(), p['nombre'], p['apellido'])
            session['username'] = p['email']
            return redirect('index')

def listadoUsers():
    if 'username' not in session:
        return redirect(url_for('accesoDenegado'))
    tabla = configuracion.get_config()
    if tabla.sitio_habilitado == 0:
        return redirect(url_for('mantenimiento'))
    lista = User.all()
    return render_template('user/listado.html', lista=lista)

def verificarSiEsAdmin():
    u = User_tiene_rol.tiene_rol(User.get_by_email(session['username']).id, Rol.get_by_nombre('administrador').id)
    if u !=None:
        return True
    else:
        return False

def showUser(id):
    if 'username' not in session:
        return redirect(url_for('accesoDenegado'))
    print(id)
    return render_template('/user/showUser.html', usuario=id)

def actualizarUser(id):
    if 'username' not in session or not session['admin']:
        return redirect(url_for('accesoDenegado'))
    return render_template('user/actualizarUser.html', user=id)

def actualizar():
    p = request.form
    act = User.get_by_email(session['username'])
    User.actualizar_username(act.username,p['user'])
    User.actualizar_password(p['user'],p['password'])
    return redirect(url_for('index'))

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
    return render_template('user/listado.html', lista=lista)

def mostrarInactivos():
    lista = User.select_inactivos()
    return render_template('user/listado.html', lista=lista)