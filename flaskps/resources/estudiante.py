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
from flaskps.models.responsable_estudiante import Responsable_Estudiante
from flaskps.models.rol import Rol
from flaskps.models.responsable import Responsable
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
    lista = Estudiante.notDeletedAll()
    eliminados = Estudiante.deletedAll()
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
        responsables=Responsable.all(),
        eliminados=eliminados
    )


def crearEstudiante():
    if 'email' not in session or not any(i in ['administrador', 'docente', 'preceptor'] for i in session['roles']):
        return redirect(url_for("accesoDenegado"))
    p = request.form
    print(p)
    if Estudiante.getByDNI(int(p['numero'])) is not None:
        return jsonify({'ok': 'no'})
    else:
        if p['nuevoResponsable'] == '0' and p['responsable'] == '0':
            return jsonify({'ok': 'faltaResp'})
        e = Estudiante.create(
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
        if p['nuevoResponsable'] == '1':
            respActID = nuevoResponsable(p)
            r = Responsable_Estudiante.get(respActID, e.id)
            if not r:
                Responsable_Estudiante.create(respActID, e.id)
        else:
            Responsable_Estudiante.create(p['responsable'], e.id)
        return jsonify({'ok': 'ok'})

def actualizarEstudiante(dni):
    if 'email' not in session or not any(i in ['administrador', 'docente', 'preceptor'] for i in session['roles']):
        return redirect(url_for("accesoDenegado"))
    p = request.form
    e = Estudiante.actualizar(
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
    r = Responsable_Estudiante.get(p['responsable'], e.id)
    if not r:
        Responsable_Estudiante.create(p['responsable'], e.id)
    flash('estudiante actualizado con exito!')
    return redirect(url_for('listadoEstudiantes'))

def nuevoResponsable(p):
    r = Responsable.create(
        p["apellidoR"],
        p["nombreR"],
        p["fechaR"],
        p["localidadR"],
        p["domicilioR"],
        p["generoR"],
        p["tipoDR"],
        p["numeroR"],
        p["telefonoR"],
    )
    return r.id