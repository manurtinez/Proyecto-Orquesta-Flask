from flaskps.db import db
from sqlalchemy import update
from datetime import datetime

class Docente_responsable_taller(db.Model):
    __tablename__ = 'ciclo_lectivo_taller'
    docente_id = db.Column(db.Integer, primary_key=True)
    ciclo_lectivo_id = db.Column(db.Integer, primary_key=True)
    taller_id = db.Column(db.Integer, primary_key=True)

    #Alta
    def create(do,ci,ta):
        elemento = Docente_responsable_taller (docente_id=do, ciclo_lectivo_id=ci, taller_id=ta)

        db.session.add (elemento)
        db.session.commit()
        return elemento