from flask import redirect, render_template, request, session, url_for, flash
from flaskps.db import db
from flaskps.models.configuracion import configuracion
from flaskps.models.usuario import User
from flaskps.resources import user

def administracion():
    if 'username' not in session or not session['admin']:
        return redirect(url_for('accesoDenegado'))
    tabla = configuracion.get_config()
    if tabla.sitio_habilitado == 0:
        return mantenimiento()
    username = session['username']
    admin = user.verificarSiEsAdmin()
    return render_template('/admin/administracion.html', admin=admin, username=username)

def editarCantElementos():
    if 'username' not in session or not session['admin']:
        return redirect(url_for('accesoDenegado'))
    if request.method == 'GET':
        cant = configuracion.get_config().cantListar
        return render_template('/admin/editarCantElementos.html', cant=cant)
    else:
        cant = request.form['cant']
        configuracion.set_cantListar(cant)
        return redirect(url_for('index'))

#informacion de la orquesta LISTO!!

def informacion():
    if 'username' not in session or not session['admin']:
        return redirect(url_for('accesoDenegado'))
    tabla = configuracion.get_config()
    if tabla.sitio_habilitado == 0:
        return mantenimiento()
    return render_template('informacion.html', titulo=tabla.titulo, descripcion=tabla.descripcion)

def mantenimiento():
    if 'username' not in session or not session['admin']:
        return redirect(url_for('accesoDenegado'))
    if 'username' in session:
        username = session['username']
        admin = user.verificarSiEsAdmin()
        return render_template('desactivar.html', username=username, admin=admin)
    else:    
        return render_template('desactivar.html')

#formulario para editar informacion

def formulario():
    if 'username' not in session or not session['admin']:
        return redirect(url_for('accesoDenegado'))
    tabla = configuracion.get_config()
    if tabla.sitio_habilitado == 0:
        return render_template('desactivar.html')
    #configuracion.set_titulo("orquesta berisso")
    if request.method == 'POST':
        titulo = request.form['titulo']
        descripcion = request.form['descripcion']
        mail =request.form['mail']
        configuracion.set_titulo(titulo)
        configuracion.set_descripcion(descripcion)
        configuracion.set_mail(mail)
        return redirect(url_for('index'))
    return render_template('/admin/editarInfo.html', titulo=tabla.titulo, descripcion=tabla.descripcion)

#desactivar el la pagina web FALTA desactivar los templates y agregar la opcion activar sitio
def desactivar():
    if 'username' not in session or not session['admin']:
        return redirect(url_for('accesoDenegado'))
    configuracion.set_habilitacion(0)
    session['sitioActivado'] = False
    return mantenimiento()

def activar():
    if 'username' not in session or not session['admin']:
        return redirect(url_for('accesoDenegado'))
    configuracion.set_habilitacion(1)
    session['sitioActivado'] = True
    return render_template('activar.html')

def eliminarUser():
    return None

def bloquearUser(id):
    return None
    # print(usuario)
    # User.desactivar_user(usuario)
    # lista = User.all()
    # return render_template('user/listado.html', lista=lista, admin=user.verificarSiEsAdmin(), username=session['username'])

def activarUser(id):
    return None
    # print(usuario)
    # User.activar_user(usuario)
    # lista = User.all()
    # return render_template('user/listado.html', lista=lista, admin=user.verificarSiEsAdmin(), username=session['username'])

def accesoDenegado():
    flash('usted no esta autorizado a esta url')
    return render_template('index.html')
 #listar los elementos de las pag FALTA implementar
#@app.route('/listar.html')
#def listar():
#    return render_template('listar.html')