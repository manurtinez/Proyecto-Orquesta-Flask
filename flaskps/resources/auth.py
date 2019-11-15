from flask import redirect, render_template, request, session, url_for, flash
from flaskps.db import db
from flaskps.models.usuario import User
from flaskps.models.rol import Rol
from flaskps.models.usuario_tiene_rol import User_tiene_rol
from flaskps.models.configuracion import configuracion
from flaskps.resources import admin, user

def login():
    return render_template('auth/login.html')

def authenticate():
    params = request.form
    usuario = User.get_by_email_and_pass(params['email'], params['password'])
    print(usuario)
    if not usuario:
        flash('credenciales invalidas')
        return redirect(url_for('login'))
    session['email'] = request.form['email']
    roles = Rol.all()
    aux = []
    for r in roles:
        if User_tiene_rol.tiene_rol(usuario.id, r.id):
            aux.append(r.nombre)
    session['roles'] = aux
    print(session['roles'])
    flash('logeo exitoso!')
    return redirect(url_for('index'))

def logout():
    session.clear()
    return redirect(url_for('index'))