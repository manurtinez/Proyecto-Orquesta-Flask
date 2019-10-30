from flask import redirect, render_template, request, session, url_for, flash
from flaskps.db import db
from flaskps.models.usuario import User
from flaskps.models.configuracion import configuracion

def login():
    tabla = configuracion.get_config()
    if tabla.sitio_habilitado == 0:
        return render_template('desactivar.html')
    return render_template('auth/login.html')

def authenticate():
    tabla = configuracion.get_config()
    if tabla.sitio_habilitado == 0:
        return render_template('desactivar.html')
    error = ''
    params = request.form
    usuario = User.get_by_email_and_pass(params['email'], params['password'])
    print(usuario)
    if not usuario:
        flash('credenciales invalidas')
        return redirect(url_for('login'))
    session['username'] = request.form['email']
    flash('logeo exitoso!')
    return redirect(url_for('index'))

def logout():
    tabla = configuracion.get_config()
    if tabla.sitio_habilitado == 0:
        return render_template('desactivar.html')
    del session['username']
    return redirect(url_for('index'))