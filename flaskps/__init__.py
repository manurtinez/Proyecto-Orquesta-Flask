from os import path
from flask import Flask, url_for, render_template, g, request, session, flash, redirect
from flaskps.models.usuario import User
from flaskps.models.configuracion import configuracion
from flaskps.models.escuela import Escuela
from flaskps.db import db
from flaskps.resources import admin, auth, user, estudiante, docente
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

#Autenticacion
app.add_url_rule('/login', 'login', auth.login)
app.add_url_rule('/logout', 'logout', auth.logout)
app.add_url_rule(
    '/authenticate',
    'authenticate',
    auth.authenticate,
    methods=['POST', 'GET']
)

#Estudiante
app.add_url_rule('/user/listadoEstudiantes', 'listadoEstudiantes', estudiante.listadoEstudiantes)
app.add_url_rule('/estudiante/actualizarEstudiante/<dni>', 'actualizarEstudiante', estudiante.actualizarEstudiante)
app.add_url_rule('/estudiante/crearEstudiante', 'crearEstudiante', estudiante.crearEstudiante, methods=['POST'])

#Docente
app.add_url_rule('/docente/listado', 'listadoDocentes', docente.listadoDocentes)
app.add_url_rule('/docente/altaDocente', 'crearDocente', docente.crearDocente, methods=['POST'])

#Usuario
app.add_url_rule('/user/registro', 'registro', user.registrar)
app.add_url_rule('/user/crear', 'crear', user.crear, methods=['POST'])
app.add_url_rule('/user/listado', 'listadoUsers', user.listadoUsers)
app.add_url_rule('/user/showUser/<id>', 'showUser', user.showUser)
app.add_url_rule('/user/buscar', 'buscarUsuario', user.buscar, methods=['POST', 'GET'])
app.add_url_rule('/user/actualizar/<m>', 'actualizar', user.actualizar, methods=['POST'])
app.add_url_rule('/user/listado/activos', 'mostrarActivos', user.mostrarActivos)
app.add_url_rule('/user/listado/inactivos', 'mostrarInactivos', user.mostrarInactivos)

#ADMINISTRACION
app.add_url_rule('/administracion', 'administracion', admin.administracion, methods=['GET', 'POST'])
#app.add_url_rule('/editarCantElementos', 'editarCantElementos', admin.editarCantElementos, methods=['GET', 'POST'])
#app.add_url_rule('/informacion', 'informacion', admin.informacion)
#app.add_url_rule('/editarInfo', 'editarInfo', admin.formulario, methods=['GET', 'POST'])
app.add_url_rule('/admin/desactivar', 'desactivar', admin.desactivar)
app.add_url_rule('/admin/activar', 'activar', admin.activar)
app.add_url_rule('/admin/activarUser/<id>', 'activarUser', admin.activarUser)
app.add_url_rule('/admin/bloquearUser/<id>', 'bloquearUser', admin.bloquearUser)
app.add_url_rule('/mantenimiento', 'mantenimiento', admin.mantenimiento)
app.add_url_rule('/eliminarUser/<email>', 'eliminarUser', admin.eliminarUser)
app.add_url_rule('/eliminarEstudiante/<dni>', 'eliminarEstudiante', admin.eliminarEstudiante)
app.add_url_rule('/eliminarDocente/<dni>', 'eliminarDocente', admin.eliminarDocente)
app.add_url_rule('/accesoDenegado', 'accesoDenegado', admin.accesoDenegado)
app.add_url_rule('/AgregarCicloLectivo', 'crearciclolectivo', admin.crearciclolectivo,methods=['GET','POST'])

@app.route('/')
def index():
    tabla = configuracion.get_config()
    if tabla.sitio_habilitado == 0:
        return redirect(url_for('mantenimiento'))
    return render_template('index.html', titulo=tabla.titulo, descripcion=tabla.descripcion, mail=tabla.mail, escuelas=Escuela.get_all()) 