from os import path
from flask import Flask, url_for, render_template, g, request, session, flash, redirect
from flaskps.models.usuario import usuario
from flaskps.db import get_db

app = Flask(__name__)
app.config.from_pyfile('config/production.py')
#Autenticacion
# app.add_url_rule('/login', 'login', login)
# app.add_url_rule('/logout', 'auth_logout', auth.logout)
# app.add_url_rule(
#     '/authenticate',
#     'auth_authenticate',
#     auth.authenticate,
#     methods=['POST']
# )

@app.route('/')
def index():
    return render_template('inicio.html')

@app.route('/login.html', methods=['POST', 'GET'])
def login():
    error = ''
    params = request.form
    if request.method == 'POST':
        usuario.db = get_db()
        #user = usuario.find_by_email_and_pass(params['email'], params['password'])
        #if request.form['password'] == '1234' and request.form['user'] == 'admin':
        if usuarios:
            session['username'] = request.form['email']
            flash('logeo exitoso!')
            return redirect(url_for('index'))
        else:
            error = 'credenciales invalidas'
    return render_template('login.html', error=error)

#administracion: conecta con la ruta area admin
@app.route('/administracion.html')
def administracion():
     return render_template('administracion.html')


@app.route('/logout')
def logout():
    session.clear()
    session['username'] = None
    return redirect(url_for('administracion.html'))

if __name__ == '__main__': 
  
    # run() method of Flask class runs the application  
    # on the local development server.
    session['username'] = None
    app.secret_key = 'hola'
    app.run()