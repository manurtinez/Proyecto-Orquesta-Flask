from flask import redirect, url_for, render_template, request, flash, session
from flaskps.models.taller import Taller
from flaskps.models.ciclo_lectivo import Ciclo_lectivo
from flaskps.models.ciclo_lectivo_taller import Ciclo_lectivo_taller
from flaskps.models.estudiante_taller import Estudiante_taller
from flaskps.models.estudiante import Estudiante
from flaskps.models.docente import Docente
from flaskps.models.configuracion import configuracion
from flaskps.models.docente_responsable_taller import Docente_responsable_taller
from flaskps.models.asistencia_estudiante_taller import Asistencia_estudiante_taller
import json, datetime


def asociacionesTalleres():
    tabla = configuracion.get_config()
    if tabla.sitio_habilitado == 0:
        return redirect(url_for("mantenimiento"))
    if 'email' not in session or 'administrador' not in session['roles']:
        return redirect(url_for('accesoDenegado'))
    ciclosTalleres = []
    t = Taller.all()
    c = Ciclo_lectivo.all()
    ct = Ciclo_lectivo_taller.all()
    for ct in ct:
        dict = {}
        aux = next((x for x in t if x.id == ct.taller_id))
        aux2 = next((x for x in c if x.id == ct.ciclo_lectivo_id))
        dict['tallerid'] = ct.taller_id
        dict['cicloid'] = ct.ciclo_lectivo_id
        dict['tallernombre'] = aux.nombre
        dict['cicloinicio'] = aux2.fecha_ini
        dict['ciclofin'] = aux2.fecha_fin
        ciclosTalleres.append(dict)
    return render_template(
        "asociacionesTalleres.html",
        talleres=Taller.all(),
        ciclos=Ciclo_lectivo.all(),
        estudiantes=Estudiante.all(),
        docentes=Docente.all(),
        ciclosTalleres=ciclosTalleres,
    )

def asociarTallerCiclo():
    tabla = configuracion.get_config()
    if tabla.sitio_habilitado == 0:
        return redirect(url_for("mantenimiento"))
    if 'email' not in session or 'administrador' not in session['roles']:
        return redirect(url_for('accesoDenegado'))
    p = request.form
    if not Ciclo_lectivo_taller.get(p['taller'], p['ciclo']):
        Ciclo_lectivo_taller.create(p["taller"], p["ciclo"])
        flash("la asociacion se hizo exitosamente")
        return redirect(url_for("asociacionesTalleres"))
    else:
        flash('Esta asociacion ya existe!')
        return redirect(url_for('asociacionesTalleres'))

def asociarTallerDocentes():
    tabla = configuracion.get_config()
    if tabla.sitio_habilitado == 0:
        return redirect(url_for("mantenimiento"))
    if 'email' not in session or 'administrador' not in session['roles']:
        return redirect(url_for('accesoDenegado'))
    d = request.form.getlist('docentes')
    c = eval(request.form['taller'])
    repetidos = False
    for d in d:
        if not Docente_responsable_taller.get(int(d), c['cicloid'], c['tallerid']):
            Docente_responsable_taller.create(int(d), c['cicloid'], c['tallerid'])
        else:
            repetidos = True
    if repetidos:
        flash('Asociacion exitosa! Nota: Algunos de los docentes ya estaban asociados')
    return redirect(url_for('asociacionesTalleres'))

def asociarTallerEstudiantes():
    tabla = configuracion.get_config()
    if tabla.sitio_habilitado == 0:
        return redirect(url_for("mantenimiento"))
    if 'email' not in session or 'administrador' not in session['roles']:
        return redirect(url_for('accesoDenegado'))
    e = request.form.getlist('estudiantes')
    c = eval(request.form['taller'])
    repetidos = False
    for e in e:
        if not Estudiante_taller.get(int(e), c['cicloid'], c['tallerid']):
            Estudiante_taller.create(int(e), c['cicloid'], c['tallerid'])
        else:
            repetidos = True
    if repetidos:
        flash('Asociacion exitosa! Nota: Algunos de los estudiantes ya estaban asociados')
    else:
        flash('Asociacion exitosa!')
    return redirect(url_for('asociacionesTalleres'))