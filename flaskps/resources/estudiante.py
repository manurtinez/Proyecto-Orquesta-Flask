from flask import (
    render_template,
    jsonify,
    abort,
    url_for,
    request,
    redirect,
    session,
    flash,
)
from flaskps.models.configuracion import configuracion
from flaskps.models.rol import Rol
from flaskps.models.usuario_tiene_rol import User_tiene_rol
from flaskps.models.escuela import Escuela
from flaskps.models.nivel import Nivel
from flaskps.models.usuario import User
from flaskps.models.barrio import Barrio
from flaskps.models.genero import Genero
from flaskps.models.estudiante import Estudiante
import json, requests


def listadoEstudiantes():
    if 'email' not in session or not any(i in ['administrador', 'docente', 'preceptor'] for i in session['roles']):
        return redirect(url_for("accesoDenegado"))
    tabla = configuracion.get_config()
    if tabla.sitio_habilitado == 0:
        return redirect(url_for("mantenimiento"))
    lista = Estudiante.all()
    try:
        dnis = requests.get(
            "https://api-referencias.proyecto2019.linti.unlp.edu.ar/tipo-documento"
        )
        localidades = requests.get(
            "https://api-referencias.proyecto2019.linti.unlp.edu.ar/localidad"
        )
        tiposDNI = json.loads(dnis.text)
        listaLoc = json.loads(localidades.text)
    except requests.exceptions.ConnectionError:
        flash('hubo un error al traer datos de los dnis y/o localidades :(')
        return redirect(url_for('index'))
    user = User.get_by_email(session['email'])
    roles = Rol.all()
    aux = []
    for r in roles:
        if User_tiene_rol.tiene_rol(user.id, r.id):
            aux.append(r.nombre)
    return render_template(
        "estudiante/listadoEstudiantes.html", lista=lista, cant=tabla.cantListar,
        escuelas=Escuela.get_all(),
        niveles=Nivel.get_all(),
        barrios=Barrio.get_all(),
        generos=Genero.get_all(),
        dnis=tiposDNI,
        localidades=listaLoc,
    )


def crearEstudiante():
    if 'email' not in session or not any(i in ['administrador', 'docente', 'preceptor'] for i in session['roles']):
        return redirect(url_for("accesoDenegado"))
    p = request.form
    if Estudiante.getByDNI(p['numero']) is not None:
        flash('ya existe un estudiante con ese numero de dni!')
        return redirect(url_for('listadoEstudiantes'))
    else:
        Estudiante.create(
            p["apellido"],
            p["nombre"],
            p["fechaN"],
            p["localidad"],
            p["nivel"],
            p["domicilio"],
            p["genero"],
            p["escuela"],
            p["tipoD"],
            p["numero"],
            p["telefono"],
            p["barrio"],
        )
        flash('estudiante creado con exito!')
        return redirect(url_for("listadoEstudiantes"))

def actualizarEstudiante(dni):
    if 'email' not in session or not any(i in ['administrador', 'docente', 'preceptor'] for i in session['roles']):
        return redirect(url_for("accesoDenegado"))
    p = request.form
    Estudiante.actualizar(
        dni,
        p["apellido"],
        p["nombre"],
        p["fechaN"],
        p["localidad"],
        p["nivel"],
        p["domicilio"],
        p["genero"],
        p["escuela"],
        p["tipoD"],
        p["telefono"],
        p["barrio"],
    )
    flash('estudiante actualizado con exito!')
    return redirect(url_for('listadoEstudiantes'))