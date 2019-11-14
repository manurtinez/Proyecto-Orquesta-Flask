from flaskps.db import db
from sqlalchemy import update
from datetime import datetime

class Ciclo_lectivo_taller(db.Model):
    __tablename__ = 'ciclo_lectivo_taller'
    taller_id = db.Column(db.Integer, primary_key=True)
    ciclo_lectivo_id = db.Column(db.Integer, primary_key=True)

    #Para añadir anexo entre taller y ciclo lectivo. Se hace con los id's de taller y ciclo.
    def create(ta,ci):
        elemento = Ciclo_lectivo_taller (taller_id=ta, ciclo_lectivo_id=ci)

        db.session.add (elemento)
        db.session.commit()
        return elemento