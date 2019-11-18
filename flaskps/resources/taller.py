from flask import redirect, url_for, render_template, request, flash
from flaskps.models.taller import Taller
from flaskps.models.ciclo_lectivo import Ciclo_lectivo
from flaskps.models.ciclo_lectivo_taller import Ciclo_lectivo_taller


def asociarTallerCiclo():
    if request.method == 'GET':
        talleres = Taller.all()
        ciclos = Ciclo_lectivo.all()
        return render_template('asociarTallerCiclo.html', talleres=talleres, ciclos=ciclos)
    elif request.method == 'POST':
        p = request.form
        Ciclo_lectivo_taller.create(p['taller'], p['ciclo'])
        flash('la asociacion se hizo exitosamente')
        return redirect(url_for('index'))