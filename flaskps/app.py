from os import path
from flask import Flask, url_for, render_template, g, request, session, flash, redirect
from flaskps.models.usuario import usuario
from flaskps.db import get_db
from flaskps.resources import admin

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
     informacion = "informacion"
     return render_template('administracion.html', informacion=informacion)

#desactivar el la pagina web FALTA desactivar los templates y agregar la opcion activar sitio
@app.route('/desactivar.html')
def desactivar():
    return render_template('desactivar.html')

#informacion de la orquesta FALTA agregarle para que el admin modifique la info
@app.route('/informacion.html')
def informacion():
    return render_template('informacion.html')

#listar los elementos de las pag FALTA implementar
@app.route('/listar.html')
def listar():
    return render_template('listar.html')


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
    app.run(debug=True)  #para que se reinicie solo el servidor