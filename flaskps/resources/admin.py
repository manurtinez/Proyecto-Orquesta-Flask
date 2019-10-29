from flask import redirect, render_template, request, session, url_for, flash
from flaskps.db import db
from flaskps.models.configuracion import configuracion

def administracion():
     return render_template('administracion.html')

#desactivar el la pagina web FALTA desactivar los templates y agregar la opcion activar sitio
#@app.route('/desactivar.html')
#def desactivar():
#    return render_template('desactivar.html')

#informacion de la orquesta LISTO!!

def informacion():
    tabla = configuracion.get_config()
    print(tabla)
    #cur = mysql.connection.cursor()
    #cur.execute('SELECT * FROM configuracion')
    #data = cur.fetchall()
    return render_template('informacion.html')



#formulario para editar informacion

def formulario():
 #    cur = mysql.connection.cursor()
 #    cur.execute('SELECT * FROM configuracion WHERE id = %s', (id))
 #    data = cur.fetchall()
     return render_template('formulario.html')

 #@app.route('/editar/<id>', methods = ['POST'])
 #def update_conf(id):
 #    if request.method == 'POST':
 #        titulo = request.form['titulo']
 #        descripcion = request.form['descripcion']
 #        mail = request.form['mail']
 #        cur = mysql.connection.cursor()
 #        cur.execute('UPDATE configuracion SET titulo = %s, descripcion = %s, mail = %s WHERE id = %s', (titulo, descripcion, mail, id))
 #        mysql.connection.commit()
 #       return redirect(url_for('administracion.html'))

 #listar los elementos de las pag FALTA implementar
#@app.route('/listar.html')
#def listar():
#    return render_template('listar.html')
