from flask import redirect, render_template, request, session, url_for, flash
from flaskps.db import db
from flaskps.models.usuario import User
from flaskps.models.rol import Rol
from flaskps.models.usuario_tiene_rol import User_tiene_rol
from flaskps.models.configuracion import configuracion
from flaskps.resources import admin, user
from flaskps.models.rol_tiene_permiso import rol_tiene_permiso
from flaskps.models.permiso import Permiso

def login():
    return render_template('auth/login.html')

def authenticate():
    tabla = configuracion.get_config()
    if tabla.sitio_habilitado == 0:
        return redirect(url_for("mantenimiento"))
    params = request.form
    usuario = User.get_by_email_and_pass(params['email'], params['password'])
    print(usuario)
    if not usuario:
        flash('credenciales invalidas')
        return redirect(url_for('login'))
    session['email'] = request.form['email']

    roles = Rol.all()
    permisos = Permiso.all()
    rolespermisos = rol_tiene_permiso.all()

    aux = []
    auxpermisos = []
    auxrp = []
    for r in roles:
        if User_tiene_rol.tiene_rol(usuario.id, r.id):
            for rp in rolespermisos: #Busca sus permisos y almacena los id's de estos en auxrp
                if r.id == rp.id_rol:
                    auxrp.append(rp.id_permiso)

            for p in permisos: #get tuplas donde p.id= rp.idpermiso
                for arp in auxrp:
                    if arp == p.id:  #Si el id del permiso es igual al del permiso actual, almaceno el nombre
                        auxpermisos.append(p.nombre)
            aux.append(r.nombre)
    session['roles'] = aux
    session ['permisos'] = auxpermisos
    flash('Sesión iniciada exitosamente!')
    return redirect(url_for('index'))

def logout():
    session.clear()
    return redirect(url_for('index'))