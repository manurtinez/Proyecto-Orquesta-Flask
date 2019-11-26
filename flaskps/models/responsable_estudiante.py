from flaskps.db import db
from sqlalchemy import PrimaryKeyConstraint, ForeignKey
from flaskps.models import responsable, estudiante

class Responsable_Estudiante(db.Model):
    __tablename__ = 'responsable_estudiante'
    __table_args__ = (
        PrimaryKeyConstraint('responsable_id', 'estudiante_id'),
        {'extend_existing': True}
    )

    responsable_id = db.Column(db.Integer, ForeignKey(responsable.Responsable.id))
    estudiante_id = db.Column(db.Integer, ForeignKey(estudiante.Estudiante.id))

    def all():
        return Responsable_Estudiante.query.all()

    def get(rid, eid):
        return Responsable_Estudiante.query.filter_by(responsable_id=rid, estudiante_id=eid).first()

    def create(rid, eid):
        e = Responsable_Estudiante (responsable_id = rid, estudiante_id = eid)

        db.session.add(e)
        db.session.commit()
        return e