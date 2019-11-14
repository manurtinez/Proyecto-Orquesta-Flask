from flask import render_template, jsonify, abort, url_for, request, redirect, session, flash
from flaskps.models import configuracion
from flaskps.models.escuela import Escuela
from flaskps.models.nivel import Nivel
from flaskps.models.usuario import User
from flaskps.models.barrio import Barrio
import json, requests


def listadoEstudiantes():
    if 'username' not in session:
        return redirect(url_for('accesoDenegado'))
    tabla = configuracion.get_config()
    if tabla.sitio_habilitado == 0:
        return redirect(url_for('mantenimiento'))
    lista = User.all()
    return render_template('user/listado.html', lista=lista, cant=tabla.cantListar)

def altaEstudiante():
    tiposDNI = []
    listaLoc = []
    dnis = requests.get('https://api-referencias.proyecto2019.linti.unlp.edu.ar/tipo-documento')
    localidades = requests.get('https://api-referencias.proyecto2019.linti.unlp.edu.ar/localidad')
    dnis = json.loads(dnis.text)
    localidades = json.loads(localidades.text)
    for i in range(len(dnis)):
        tiposDNI.append(dnis[i]['nombre'])
    for i in range(len(localidades)):
        listaLoc.append(localidades[i]['nombre'])
    print(tiposDNI)
    return render_template('/estudiante/altaEstudiante.html', escuelas=Escuela.get_all(), niveles=Nivel.get_all(),
     barrios=Barrio.get_all(), dnis=tiposDNI, localidades=listaLoc)

def crearEstudiante():
    return None