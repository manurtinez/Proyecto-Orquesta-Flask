from os import path
from flask import Flask, url_for, render_template, g, request, session, flash, redirect
from flaskps.models.usuario import User
from flaskps.resources import user
from flaskps.db import db
from flaskps.resources import admin, auth
from flaskps.config import Config
#from flask_mysqldb import MySQL #xampp coneccion bd

app = Flask(__name__)
app.config.from_object(Config)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://"+Config.DB_USER+":"+Config.DB_PASS+"@"+Config.DB_HOST+"/"+Config.DB_NAME
db.init_app(app)

#Conexion a la base de datos para xampp instalar: pip install flask-mysqldb
#app.config['MYSQL_HOST'] = 'localhost'
#app.config['MYSQL_USER'] = 'root'
#app.config['MYSQL_PASSWORD'] = 'root'
#app.config['MYSQL_DB'] = 'grupo36'
#mysql = MySQL(app)

#settings
#app.secret_key = 'mysecretkey'

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
#app.add_url_rule('/user/registro', 'registro', user.registrar)
app.add_url_rule('/user/crear', 'crear', user.crear, methods=['POST'])
app.add_url_rule('/user/listado', 'listadoUsers', user.listadoUsers)

@app.route('/')
def index():
    return render_template('inicio.html')

@app.route('/registro.html', methods=['POST', 'GET'])
def registro():
    return render_template('/user/registro.html')

#ADMINISTRACION
app.add_url_rule('/administracion.html', 'administracion', admin.administracion)
app.add_url_rule('/informacion.html', 'informacion', admin.informacion)
 #@app.route('/<id>')
app.add_url_rule('/formulario.html', 'formulario', admin.formulario)



if __name__ == '__main__': 
  
    # run() method of Flask class runs the application  
    # on the local development server.
    session['username'] = None
    app.secret_key = 'hola'
    app.run(debug = True)  #para que se reinicie solo el servidor