from flask import redirect, render_template, request, session, url_for, flash
from flaskps.db import db
from flaskps.models.usuario import User
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
    session['admin'] = user.verificarSiEsAdmin()
    flash('logeo exitoso!')
    return redirect(url_for('index'))

def logout():
    del session['email']
    del session['admin']
    return redirect(url_for('index'))