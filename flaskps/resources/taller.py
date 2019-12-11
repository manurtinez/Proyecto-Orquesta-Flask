from flask import redirect, url_for, render_template, request, flash, session, jsonify
from flaskps.models.taller import Taller
from flaskps.models.ciclo_lectivo import Ciclo_lectivo
from flaskps.models.ciclo_lectivo_taller import Ciclo_lectivo_taller
from flaskps.models.estudiante_taller import Estudiante_taller
from flaskps.models.estudiante import Estudiante
from flaskps.models.nucleo import Nucleo
from flaskps.models.docente import Docente
from flaskps.models.configuracion import configuracion
from flaskps.models.docente_responsable_taller import Docente_responsable_taller
from flaskps.models.asistencia_estudiante_taller import Asistencia_estudiante_taller
from flaskps.models.horarios_nucleos_docentes import Horarios_Nucleos_Docentes
import json
import datetime


def asociacionesTalleres():
    tabla = configuracion.get_config()
    if tabla.sitio_habilitado == 0:
        return redirect(url_for("mantenimiento"))
    if "email" not in session or "administrador" not in session["roles"]:
        return redirect(url_for("accesoDenegado"))
    ciclosTalleres = []
    t = Taller.all()
    c = Ciclo_lectivo.all()
    ct = Ciclo_lectivo_taller.all()
    for ct in ct:
        dict = {}
        aux = next((x for x in t if x.id == ct.taller_id))
        aux2 = next((x for x in c if x.id == ct.ciclo_lectivo_id))
        dict["tallerid"] = ct.taller_id
        dict["cicloid"] = ct.ciclo_lectivo_id
        dict["tallernombre"] = aux.nombre
        dict["cicloinicio"] = aux2.fecha_ini
        dict["semestre"] = aux2.semestre
        ciclosTalleres.append(dict)
    return render_template(
        "asociacionesTalleres.html",
        talleres=Taller.all(),
        ciclos=Ciclo_lectivo.all(),
        estudiantes=Estudiante.all(),
        docentes=Docente.all(),
        ciclosTalleres=ciclosTalleres,
    )


def devolverEstudiantes():
    ct = eval(request.json["val"])
    lista = buscarctEst(ct["cicloid"], ct["tallerid"])
    return jsonify({"lista": lista})


def buscarctEst(idciclo, idtaller):
    et = Estudiante_taller.all()
    lista = []
    for et in et:
        if et.ciclo_lectivo_id == idciclo and et.taller_id == idtaller:
            lista.append(et.estudiante_id)
    return lista


def devolverDocentes():
    ct = eval(request.json["val"])
    lista = buscarctDoc(ct["cicloid"], ct["tallerid"])
    return jsonify({"lista": lista})


def buscarctDoc(idciclo, idtaller):
    dt = Docente_responsable_taller.all()
    lista = []
    for dt in dt:
        if dt.ciclo_lectivo_id == idciclo and dt.taller_id == idtaller:
            lista.append(dt.docente_id)
    return lista


def tallerSeleccionado():
    id = int(request.json["id"])
    ct = Ciclo_lectivo_taller.all()
    act = next((x for x in ct if x.taller_id == id), None)
    cicloid = buscarCiclo(id)
    return jsonify({"idciclo": cicloid})


def buscarCiclo(idTaller):
    ct = Ciclo_lectivo_taller.all()
    act = next((x for x in ct if x.taller_id == idTaller), None)
    if act:
        ciclo = Ciclo_lectivo.getByid(act.ciclo_lectivo_id)
        return ciclo.id
    else:
        return -1


def asociarTallerCiclo():
    tabla = configuracion.get_config()
    if tabla.sitio_habilitado == 0:
        return redirect(url_for("mantenimiento"))
    if "email" not in session or "administrador" not in session["roles"]:
        return redirect(url_for("accesoDenegado"))
    p = request.form
    if not Ciclo_lectivo_taller.get(p["taller"], p["ciclo"]):
        # Ciclo_lectivo_taller.delete()
        Ciclo_lectivo_taller.create(p["taller"], p["ciclo"])
        flash("la asociacion se hizo exitosamente")
        return redirect(url_for("asociacionesTalleres"))
    else:
        flash("Esta asociacion ya existe!")
        return redirect(url_for("asociacionesTalleres"))


def asociarTallerDocentes():
    tabla = configuracion.get_config()
    if tabla.sitio_habilitado == 0:
        return redirect(url_for("mantenimiento"))
    if "email" not in session or "administrador" not in session["roles"]:
        return redirect(url_for("accesoDenegado"))
    d = request.form.getlist("docentes")
    c = eval(request.form["taller"])
    repetidos = False
    for d in d:
        if not Docente_responsable_taller.get(int(d), c["cicloid"], c["tallerid"]):
            e = Docente_responsable_taller.create(int(d), c["cicloid"], c["tallerid"])
        else:
            repetidos = True
    if repetidos:
        flash("Asociacion exitosa! Nota: Algunos de los docentes ya estaban asociados")
    # aca habria que setear el nucleo que corresponsa, 1 era de prueba
    Docente_responsable_taller.setNucleo(int(d), c["cicloid"], c["tallerid"], 1)
    return redirect(url_for("asociacionesTalleres"))


def asociarTallerEstudiantes():
    tabla = configuracion.get_config()
    if tabla.sitio_habilitado == 0:
        return redirect(url_for("mantenimiento"))
    if "email" not in session or "administrador" not in session["roles"]:
        return redirect(url_for("accesoDenegado"))
    e = request.form.getlist("estudiantes")
    c = eval(request.form["taller"])
    repetidos = False
    for e in e:
        if not Estudiante_taller.get(int(e), c["cicloid"], c["tallerid"]):
            Estudiante_taller.create(int(e), c["cicloid"], c["tallerid"])
        else:
            repetidos = True
    if repetidos:
        flash(
            "Asociacion exitosa! Nota: Algunos de los estudiantes ya estaban asociados"
        )
    else:
        flash("Asociacion exitosa!")
    return redirect(url_for("asociacionesTalleres"))


def asignarHorarios():
    tabla = configuracion.get_config()
    if tabla.sitio_habilitado == 0:
        return redirect(url_for("mantenimiento"))
    if "email" not in session or (
        "administrador" not in session["roles"] and "docente" not in session["roles"]
    ):
        return redirect(url_for("accesoDenegado"))
    ciclosTalleres = []
    t = Taller.all()
    c = Ciclo_lectivo.all()
    ct = Ciclo_lectivo_taller.all()
    for ct in ct:
        dict = {}
        aux = next((x for x in t if x.id == ct.taller_id))
        aux2 = next((x for x in c if x.id == ct.ciclo_lectivo_id))
        dict["tallerid"] = ct.taller_id
        dict["cicloid"] = ct.ciclo_lectivo_id
        dict["tallernombre"] = aux.nombre
        dict["cicloinicio"] = aux2.fecha_ini
        dict["semestre"] = aux2.semestre
        ciclosTalleres.append(dict)
    if request.method == "GET":
        return render_template(
            "asignarHorarios.html",
            docentes=Docente.all(),
            ciclosTalleres=ciclosTalleres,
            nucleos=Nucleo.get_all(),
        )
    else:
        p = request.form
        ct = eval(p["tallerciclo"])
        dt = Docente_responsable_taller.get(p["docente"], ct["cicloid"], ct["tallerid"])
        if not dt:
            dt = Docente_responsable_taller.create(
                p["docente"], ct["cicloid"], ct["tallerid"]
            )
        hnd = Horarios_Nucleos_Docentes.getByInfo(dt.docente_id, dt.ciclo_lectivo_id, dt.taller_id, p["nucleo"], p["dia"])
        if hnd:
            flash('la asociacion ya existe!')
        else:
            Horarios_Nucleos_Docentes.create(dt.docente_id, dt.ciclo_lectivo_id, dt.taller_id, p["nucleo"], p["dia"])
            flash("nucleo y dia asociados con exito!")
        return render_template(
            "asignarHorarios.html",
            docentes=Docente.all(),
            ciclosTalleres=ciclosTalleres,
            nucleos=Nucleo.get_all(),
        )

def verHorarios():
    tabla = configuracion.get_config()
    if tabla.sitio_habilitado == 0:
        return redirect(url_for("mantenimiento"))
    if "email" not in session or (
        "administrador" not in session["roles"] and "docente" not in session["roles"]
    ):
        return redirect(url_for("accesoDenegado"))
    hnd = Horarios_Nucleos_Docentes.all()
    print(hnd)
    info = []
    for hnd in hnd:
        dict = {}
        dict['id'] = hnd.id
        dict['docente'] = Docente.get(hnd.docente_id)
        dict['taller'] = Taller.get(hnd.taller_id)
        dict['ciclo'] = Ciclo_lectivo.getByid(hnd.ciclo_lectivo_id)
        dict['nucleo'] = Nucleo.get_by_id(hnd.nucleo_id)
        dict['dia'] = hnd.dia
        info.append(dict)
    print(info)
    return render_template(
        "listadoHorarios.html",
        info=info,
        cant=tabla.cantListar,
    )

def desasociarHorario():
    id = request.json['id']
    print(id)
    Horarios_Nucleos_Docentes.delete(id)
    return jsonify({'ok': 'ok'})