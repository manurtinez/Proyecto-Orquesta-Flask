from flaskps.db import db
from sqlalchemy import update
from datetime import datetime

class Estudiante_taller(db.Model):
    __tablename__ = 'estudiante_taller'
    __table_args__ = (
        PrimaryKeyConstraint('estudiante_id', 'ciclo_lectivo_id','taller_id'),
    )

    estudiante_id = db.Column(db.Integer, ForeignKey(Estudiante.id))
    ciclo_lectivo_id = db.Column(db.Integer, ForeignKey(Ciclo_lectivo.id))
    taller_id = db.Column(db.Integer, ForeignKey(Taller.id))

    #Alta
    def create(es,ci,ta):
        elemento = Docente_responsable_taller (estudiante_id=do, ciclo_lectivo_id=ci, taller_id=ta)

        db.session.add (elemento)
        db.session.commit()
        return elemento
    
    #Read (devuelve todo)
    def all():
        return Estudiante_taller.query.all()
