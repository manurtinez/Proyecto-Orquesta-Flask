from flaskps.db import db
from sqlalchemy import ForeignKey, PrimaryKeyConstraint
from flaskps.models import estudiante, taller, ciclo_lectivo


class Asistencia_estudiante_taller(db.Model):
    __tablename__ = 'asistencia_estudiante_taller'

    id = db.Column(db.Integer, primary_key=True)
    estudiante_id = db.Column(db.Integer, ForeignKey(estudiante.Estudiante.id))
    ciclo_lectivo_id = db.Column(db.Integer, ForeignKey(ciclo_lectivo.Ciclo_lectivo.id))
    taller_id = db.Column(db.Integer, ForeignKey(taller.Taller.id))
    fecha = db.Column(db.String)

    def all():
        return Asistencia_estudiante_taller.query.all()

    def get(eid, cid, taid):
        return Asistencia_estudiante_taller.query.filter_by(estudiante_id=eid, ciclo_lectivo_id=cid, taller_id=taid).first()

    def create(eid, cid, taid):
        elemento = Asistencia_estudiante_taller (estudiante_id=eid, taller_id=taid, ciclo_lectivo_id=cid)
        db.session.add (elemento)
        db.session.commit()
        return elemento
