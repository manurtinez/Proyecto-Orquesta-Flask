from flask import redirect, render_template, request, session, url_for, flash
from flaskps.db import db
from flaskps.models.configuracion import configuracion
from flaskps.models.usuario import User
from flaskps.models.estudiante import Estudiante
from flaskps.resources import user
from flaskps.models.ciclo_lectivo import Ciclo_lectivo

def administracion():
    if 'username' not in session or not session['admin']:
        return redirect(url_for('accesoDenegado'))
    tabla = configuracion.get_config()
    if tabla.sitio_habilitado == 0:
        return render_template('/admin/desactivar.html')
    #configuracion.set_titulo("orquesta berisso")
    if request.method == 'POST':
        titulo = request.form['titulo']
        descripcion = request.form['descripcion']
        mail =request.form['mail']
        cantListar=request.form['cantListar']
        configuracion.set_titulo(titulo)
        configuracion.set_descripcion(descripcion)
        configuracion.set_mail(mail)
        configuracion.set_cantListar(cantListar)
        return redirect(url_for('index'))
    return render_template('/admin/administracion.html', titulo=tabla.titulo, descripcion=tabla.descripcion, mail=tabla.mail, cantListar=tabla.cantListar)

#def editarCantElementos():
 #   if 'username' not in session or not session['admin']:
 #       return redirect(url_for('accesoDenegado'))
 #   if request.method == 'GET':
 #       cant = configuracion.get_config().cantListar
 #       return render_template('/admin/editarCantElementos.html', cant=cant)
 #   else:
 #       cant = request.form['cant']
 #       configuracion.set_cantListar(cant)
 #       return redirect(url_for('index'))

#informacion de la orquesta LISTO!!

#def informacion():
#    if 'username' not in session or not session['admin']:
#        return redirect(url_for('accesoDenegado'))
#    tabla = configuracion.get_config()
#    cant = configuracion.get_config().cantListar
#    if tabla.sitio_habilitado == 0:
#        return mantenimiento()
#    return render_template('informacion.html', titulo=tabla.titulo, descripcion=tabla.descripcion, mail=tabla.mail, cant=cant)

def mantenimiento():
    if 'username' not in session or not session['admin']:
        return redirect(url_for('accesoDenegado'))
    if 'username' in session:
        return render_template('/admin/desactivar.html')
    else:    
        return render_template('/admin/desactivar.html')

#formulario para editar informacion

#def formulario():
#    if 'username' not in session or not session['admin']:
#        return redirect(url_for('accesoDenegado'))
#    tabla = configuracion.get_config()
#    if tabla.sitio_habilitado == 0:
#        return render_template('desactivar.html')
    #configuracion.set_titulo("orquesta berisso")
#    if request.method == 'POST':
#        titulo = request.form['titulo']
#        descripcion = request.form['descripcion']
#        mail =request.form['mail']
#        cantListar=request.form['cantListar']
#        configuracion.set_titulo(titulo)
#        configuracion.set_descripcion(descripcion)
#        configuracion.set_mail(mail)
#        configuracion.set_cantListar(cantListar)
#        return redirect(url_for('index'))
#    return render_template('/admin/editarInfo.html', titulo=tabla.titulo, descripcion=tabla.descripcion, mail=tabla.mail, cantListar=tabla.cantListar)

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

def eliminarUser(email):
    if session['email'] != email:
        User.eliminar_usuario(email)
        flash('el usuario ha sido eliminado')
        return redirect(url_for('listadoUsers'))
    else:
        flash('no se puede eliminar a usted mismo!')
        return redirect(url_for('listadoUsers'))

def eliminarEstudiante(dni):
    Estudiante.eliminar_estudiante(dni)
    flash('el usuario ha sido eliminado')
    return redirect(url_for('listadoEstudiantes'))

def bloquearUser(id):
    if 'username' not in session or not session['admin']:
        return redirect(url_for('accesoDenegado'))
    user = User.desactivar_user(User.get_by_id(id).username)
    print(user.activo)
    return redirect(url_for('listadoUsers'))
    # print(usuario)
    # User.desactivar_user(usuario)
    # lista = User.all()
    # return render_template('user/listado.html', lista=lista, admin=user.verificarSiEsAdmin(), username=session['email'])

def activarUser(id):
    if 'username' not in session or not session['admin']:
        return redirect(url_for('accesoDenegado'))
    user = User.activar_user(User.get_by_id(id).username)
    print(user.activo)
    return redirect(url_for('listadoUsers'))
    # print(usuario)
    # User.activar_user(usuario)
    # lista = User.all()
    # return render_template('user/listado.html', lista=lista, admin=user.verificarSiEsAdmin(), username=session['email'])

def accesoDenegado():
    flash('Usted no posee autorizacion para acceder a esta url')
    return redirect(url_for('index'))
 #listar los elementos de las pag FALTA implementar
#@app.route('/listar.html')
#def listar():
#    return render_template('listar.html')

def crearciclolectivo():
    param = request.form
    
    Ciclo_lectivo.create(param['inicio'], param['fin'],param['semestre'])

    flash('El ciclo lectivo se generó exitosamente')
    return redirect(url_for('index'))