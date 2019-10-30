from flask import redirect, render_template, request, session, url_for, flash
from flaskps.db import db
from flaskps.models.configuracion import configuracion

def administracion():
    tabla = configuracion.get_config()
    if tabla.sitio_habilitado == 0:
        return render_template('desactivar.html') 
    return render_template('administracion.html')



#informacion de la orquesta LISTO!!

def informacion():
    tabla = configuracion.get_config()
    if tabla.sitio_habilitado == 0:
        return render_template('desactivar.html')
    return render_template('informacion.html', titulo=tabla.titulo, descripcion=tabla.descripcion)



#formulario para editar informacion

def formulario():
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
    return render_template('formulario.html', titulo=tabla.titulo, descripcion=tabla.descripcion)

#desactivar el la pagina web FALTA desactivar los templates y agregar la opcion activar sitio
def desactivar():
    configuracion.set_habilitacion(0)
    return render_template('desactivar.html')

def activar():
    configuracion.set_habilitacion(1)
    return render_template('activar.html')

def bloquearUser():
    return None

def activarUser():
    return None


 #listar los elementos de las pag FALTA implementar
#@app.route('/listar.html')
#def listar():
#    return render_template('listar.html')