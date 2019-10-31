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
    tabla = configuracion.get_config()
    if tabla.sitio_habilitado == 0:
        return redirect(url_for('mantenimiento'))
    lista = User.all()
    return render_template('user/listado.html', lista=lista, admin=verificarSiEsAdmin(), username=session['username'])

def verificarSiEsAdmin():
    u = User_tiene_rol.tiene_rol(User.get_by_email(session['username']).id, Rol.get_by_nombre('administrador').id)
    if u !=None:
        return True
    else:
        return False

def showUser():
    #implementar modal para info
    return(render_template('inicio.html'))

def buscar():
    nombre = request.form['nombre']
    if nombre == 'activo':
        lista = User.select_activos()
    elif nombre == 'inactivo':
        lista = User.select_inactivos()
    else:
        user = User.get_by_username(nombre)
        if user:
            lista = []
            lista.append(user)
        else:
            lista = User.all()
    return render_template('user/listado.html', lista=lista, admin=verificarSiEsAdmin(), username=session['username'])