from flask import redirect, render_template, request, session, url_for, flash
from flaskps.db import db
from flaskps.models.usuario import User

def login():
    return render_template('auth/login.html')

def authenticate():
    error = ''
    params = request.form
    usuario = User.get_by_email_and_pass(params['email'], params['password'])
    print(usuario)
    if not usuario:
        error = 'credenciales invalidas'
        return render_template('login.html', error=error)
    session['username'] = request.form['email']
    flash('logeo exitoso!')
    return redirect(url_for('index'))

def logout():
    session.clear()
    session['username'] = None
    return redirect(url_for('index'))