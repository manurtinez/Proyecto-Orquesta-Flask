from flaskps.db import db
from sqlalchemy import update, ForeignKey, PrimaryKeyConstraint
from flaskps.models import estudiante, ciclo_lectivo, taller
from datetime import datetime

class Estudiante_taller(db.Model):
    __tablename__ = 'estudiante_taller'
    __table_args__ = (
        PrimaryKeyConstraint('estudiante_id', 'ciclo_lectivo_id','taller_id'),
    )

    estudiante_id = db.Column(db.Integer, ForeignKey(estudiante.Estudiante.id))
    ciclo_lectivo_id = db.Column(db.Integer, ForeignKey(ciclo_lectivo.Ciclo_lectivo.id))
    taller_id = db.Column(db.Integer, ForeignKey(taller.Taller.id))

    #Alta
    def create(es,ci,ta):
        elemento = Estudiante_taller (estudiante_id=es, ciclo_lectivo_id=ci, taller_id=ta)

        db.session.add (elemento)
        db.session.commit()
        return elemento
    
    #Read (devuelve todo)
    def all():
        return Estudiante_taller.query.all()

    def get(eid, cid, taid):
        return Estudiante_taller.query.filter_by(estudiante_id=eid, ciclo_lectivo_id=cid, taller_id=taid).first()
