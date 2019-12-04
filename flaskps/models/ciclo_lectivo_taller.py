from flaskps.db import db
from sqlalchemy import update, ForeignKey, PrimaryKeyConstraint
from flaskps.models.taller import Taller
from flaskps.models.ciclo_lectivo import Ciclo_lectivo
from datetime import datetime
from sqlalchemy.sql.expression import Tuple

class Ciclo_lectivo_taller(db.Model):
    __tablename__ = 'ciclo_lectivo_taller'
    __table_args__ = (
        PrimaryKeyConstraint('taller_id', 'ciclo_lectivo_id'),
    )

    taller_id = db.Column(db.Integer, ForeignKey(Taller.id))
    ciclo_lectivo_id = db.Column(db.Integer, ForeignKey(Ciclo_lectivo.id))

    #Para añadir anexo entre taller y ciclo lectivo. Se hace con los id's de taller y ciclo.
    def create(ta,ci):
        elemento = Ciclo_lectivo_taller (taller_id=ta, ciclo_lectivo_id=ci)

        db.session.add (elemento)
        db.session.commit()
        return elemento

    #Read (devuelve todo)
    def all():
        return Ciclo_lectivo_taller.query.all()

    def delete(tid, cid):
        elemento = Ciclo_lectivo_taller.query.filter_by(taller_id=tid, ciclo_lectivo_id=cid).first()
        db.session.delete(elemento)
        db.session.commit()

    def get(tid, cid):
        return Ciclo_lectivo_taller.query.filter_by(taller_id=tid, ciclo_lectivo_id=cid).first()
        #return db.session.query(Ciclo_lectivo_taller).filter(
        #    Tuple(Ciclo_lectivo_taller.taller_id, Ciclo_lectivo_taller.ciclo_lectivo_id).in_([(tid, cid)])).all()