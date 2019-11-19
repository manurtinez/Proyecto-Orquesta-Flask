from flask import redirect, url_for, render_template, request, flash
from flaskps.models.taller import Taller
from flaskps.models.ciclo_lectivo import Ciclo_lectivo
from flaskps.models.ciclo_lectivo_taller import Ciclo_lectivo_taller
from flaskps.models.estudiante import Estudiante
from flaskps.models.docente import Docente
from flaskps.models.docente_responsable_taller import Docente_responsable_taller


def asociarTallerCiclo():
    if request.method == "GET":
        return render_template(
            "asociarTallerCiclo.html",
            talleres=Taller.all(),
            ciclos=Ciclo_lectivo.all(),
            estudiantes=Estudiante.all(),
            docentes=Docente.all(),
        )
    elif request.method == "POST":
        p = request.form.getlist('ciclo')
        print(p)
        #Ciclo_lectivo_taller.create(p["taller"], p["ciclo"])
        flash("la asociacion se hizo exitosamente")
        return redirect(url_for("index"))

def asociarTallerDocentes():
    d = request.form.getlist('docentes')
    for d in d:
        Docente_responsable_taller.create
    return redirect(url_for('asociarTallerCiclo'))