from flask import redirect, url_for, render_template, request, flash
from flaskps.models.taller import Taller
from flaskps.models.ciclo_lectivo import Ciclo_lectivo
from flaskps.models.ciclo_lectivo_taller import Ciclo_lectivo_taller
from flaskps.models.estudiante import Estudiante
from flaskps.models.docente import Docente
from flaskps.models.docente_responsable_taller import Docente_responsable_taller
import ast


def asociarTallerCiclo():
    if request.method == "GET":
        #ciclosTalleres = []
        t = Taller.all()
        c = Ciclo_lectivo.all()
        ct = Ciclo_lectivo_taller.all()
        # for ct in ct:
        #     dict = {}
        #     aux = next((x for x in t if x.id == ct.taller_id))
        #     aux2 = next((x for x in c if x.id == ct.ciclo_lectivo_id))
        #     dict['tallerid'] = ct.taller_id
        #     dict['cicloid'] = ct.ciclo_lectivo_id
        #     dict['tallernombre'] = aux.nombre
        #     dict['cicloinicio'] = aux2.fecha_ini
        #     dict['ciclofin'] = aux2.fecha_fin
        #     ciclosTalleres.append(dict)
        return render_template(
            "asociarTallerCiclo.html",
            talleres=Taller.all(),
            ciclos=Ciclo_lectivo.all(),
            estudiantes=Estudiante.all(),
            docentes=Docente.all(),
            # ciclosTalleres=ciclosTalleres,
        )
    elif request.method == "POST":
        p = request.form
        if not Ciclo_lectivo_taller.get(p['taller'], p['ciclo']):
            Ciclo_lectivo_taller.create(p["taller"], p["ciclo"])
            flash("la asociacion se hizo exitosamente")
            return redirect(url_for("index"))
        else:
            flash('Esta asociacion ya existe!')
            return redirect(url_for('asociarTallerCiclo'))

def asociarTallerDocentes():
    d = request.form.getlist('docentes')
    f = request.form
    # c = request.form['taller']
    # j = ast.literal_eval(c)
    for d in d:
        Docente_responsable_taller.create(int(d), f['ciclo'], f['taller'])
    return redirect(url_for('asociarTallerCiclo'))

def asociarTallerEstudiantes():
    if request.method == "GET":
        # ct = Ciclo_lectivo_taller.all()
        # t = Taller.all()
        # c = Ciclo_lectivo.all()
        # ciclosTalleres = {}
        # for ct in ct:
        #     aux = next((x for x in t if x.id == ct.taller_id))
        #     aux2 = next((x for x in c if x.id == ct.ciclo_lectivo_id))
        #     ciclosTalleres[ct.taller_id] = '{} - Inicio: {} - Fin: {}'.format()
        return render_template(
            'asociarTallerEstudiantes.html',
            ciclosTalleres = Ciclo_lectivo_taller.all(),
            talleres=Taller.all(),
            ciclos = Ciclo_lectivo.all(),
            estudiantes = Estudiante.all()
        )