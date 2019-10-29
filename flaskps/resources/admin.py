from flask import redirect, render_template, request, session, url_for, flash
from flaskps.db import db
from flaskps.models.configuracion import configuracion

def administracion():
     return render_template('administracion.html')



#informacion de la orquesta LISTO!!

def informacion():
    tabla = configuracion.get_config()
    return render_template('informacion.html', tabla=tabla)



#formulario para editar informacion

def formulario():
    #configuracion.set_titulo("orquesta berisso")
    if request.method == 'POST':
        titulo = request.form['titulo']
        descripcion = request.form['descripcion']
        mail =request.form['mail']
        configuracion.set_titulo(titulo)
        configuracion.set_descripcion(descripcion)
        configuracion.set_mail(mail)

    return render_template('formulario.html')

 

 #listar los elementos de las pag FALTA implementar
#@app.route('/listar.html')
#def listar():
#    return render_template('listar.html')

#desactivar el la pagina web FALTA desactivar los templates y agregar la opcion activar sitio
#@app.route('/desactivar.html')
#def desactivar():
#    return render_template('desactivar.html')
