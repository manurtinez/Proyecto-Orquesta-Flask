from os import path
from flask import Flask, url_for, render_template, g, request, session, flash, redirect
from flaskps.models.usuario import User
from flaskps.models.configuracion import configuracion
from flaskps.resources import user
from flaskps.db import db
from flaskps.resources import admin, auth
from flaskps.config import Config
from flask_session import Session
#from flask_mysqldb import MySQL #xampp coneccion bd

#instancio app
app = Flask(__name__)
app.config.from_object(Config)

#session
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

#config db
app.secret_key = 'hola'
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://"+Config.DB_USER+":"+Config.DB_PASS+"@"+Config.DB_HOST+"/"+Config.DB_NAME
db.init_app(app)

#Conexion a la base de datos para xampp instalar: pip install flask-mysqldb
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'root'
# app.config['MYSQL_DB'] = 'grupo36'
# mysql = MySQL(app)

#settings
# app.secret_key = 'mysecretkey'

#Autenticacion
app.add_url_rule('/login', 'login', auth.login)
app.add_url_rule('/logout', 'logout', auth.logout)
app.add_url_rule(
    '/authenticate',
    'authenticate',
    auth.authenticate,
    methods=['POST', 'GET']
)

#Usuario
app.add_url_rule('/user/registro', 'registro', user.registrar)
app.add_url_rule('/user/crear', 'crear', user.crear, methods=['POST'])
app.add_url_rule('/user/listado', 'listadoUsers', user.listadoUsers)
app.add_url_rule('/user/showUser', 'showUser', user.showUser)
app.add_url_rule('/user/buscar', 'buscarUsuario', user.buscar, methods=['POST'])

#ADMINISTRACION
app.add_url_rule('/administracion', 'administracion', admin.administracion)
app.add_url_rule('/informacion', 'asdf', admin.informacion)
app.add_url_rule('/formulario', 'editarInfo', admin.formulario, methods=['GET', 'POST'])
app.add_url_rule('/desactivar', 'desactivar', admin.desactivar)
app.add_url_rule('/activar', 'activar', admin.activar)
app.add_url_rule('/admin/activarUser', 'activarUser', admin.activarUser)
app.add_url_rule('/admin/bloquearUser', 'bloquearUser', admin.bloquearUser)

@app.route('/')
def index():
    tabla = configuracion.get_config()
    if tabla.sitio_habilitado == 0:
        return render_template('desactivar.html')
    if 'username' in session:
        username = session['username']
        return render_template('inicio.html', titulo=tabla.titulo, descripcion=tabla.descripcion, user=username)
    else:    
        return render_template('inicio.html', titulo=tabla.titulo, descripcion=tabla.descripcion)

# @app.route('/registro.html', methods=['POST', 'GET'])
# def registro():
#     return render_template('/user/registro.html')

#ADMINISTRACION: conecta con la ruta area admin
#@app.route('/administracion.html')
#def administracion():
#     informacion = "Informacion de la Orquesta"
#     return render_template('administracion.html', informacion=informacion)

#desactivar el la pagina web FALTA desactivar los templates y agregar la opcion activar sitio
#@app.route('/desactivar.html')
#def desactivar():
#    return render_template('desactivar.html')

#informacion de la orquesta LISTO!!
# @app.route('/informacion.html', methods=['POST', 'GET'])
# def informacion():
#     cur = mysql.connection.cursor()
#     cur.execute('SELECT * FROM configuracion')
#     data = cur.fetchall()
#     return render_template('informacion.html', contacts = data)

#listar los elementos de las pag FALTA implementar
#@app.route('/listar.html')
#def listar():
#    return render_template('listar.html')

#formulario para editar informacion
# @app.route('/formulario.html/<id>')
# def formulario(id):
#     cur = mysql.connection.cursor()
#     cur.execute('SELECT * FROM configuracion WHERE id = %s', (id))
#     data = cur.fetchall()
#     return render_template('formulario.html', contact = data[0])

# @app.route('/editar/<id>', methods = ['POST'])
# def update_conf(id):
#     if request.method == 'POST':
#         titulo = request.form['titulo']
#         descripcion = request.form['descripcion']
#         mail = request.form['mail']
#         cur = mysql.connection.cursor()
#         cur.execute('UPDATE configuracion SET titulo = %s, descripcion = %s, mail = %s WHERE id = %s', (titulo, descripcion, mail, id))
#         mysql.connection.commit()
#         return redirect(url_for('administracion.html'))