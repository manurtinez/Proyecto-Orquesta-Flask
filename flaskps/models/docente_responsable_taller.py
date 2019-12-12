from flaskps.db import db
from sqlalchemy import update, PrimaryKeyConstraint, ForeignKey
from flaskps.models.docente import Docente
from flaskps.models.ciclo_lectivo import Ciclo_lectivo
from flaskps.models.nucleo import Nucleo
from flaskps.models.taller import Taller
from datetime import datetime

class Docente_responsable_taller(db.Model):
    __tablename__ = 'docente_responsable_taller'
    __table_args__ = (
        PrimaryKeyConstraint('docente_id', 'ciclo_lectivo_id','taller_id'),
    )

    docente_id = db.Column(db.Integer, ForeignKey(Docente.id))
    ciclo_lectivo_id = db.Column(db.Integer, ForeignKey(Ciclo_lectivo.id))
    taller_id = db.Column(db.Integer, ForeignKey(Taller.id))

    #Alta
    def create(do,ci,ta):
        elemento = Docente_responsable_taller (docente_id=do, ciclo_lectivo_id=ci, taller_id=ta)
        db.session.add (elemento)
        db.session.commit()
        return elemento

    #Read (devuelve todo)
    def all():
        return Docente_responsable_taller.query.all()

    def setNucleo(do, ci, ta, nid):
        e = Docente_responsable_taller.query.filter_by(docente_id=do, ciclo_lectivo_id=ci, taller_id=ta).first()
        e.nucleo_id = nid
        db.session.commit()
        return e

    def get(do, ci, ta):
        return Docente_responsable_taller.query.filter_by(docente_id=do, ciclo_lectivo_id=ci, taller_id=ta).first()