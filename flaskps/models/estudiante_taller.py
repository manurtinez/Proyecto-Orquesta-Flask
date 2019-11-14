from flaskps.db import db
from sqlalchemy import update
from datetime import datetime

class Estudiante_taller(db.Model):
    __tablename__ = 'estudiante_taller'
    estudiante_id = db.Column(db.Integer, primary_key=True)
    ciclo_lectivo_id = db.Column(db.Integer, primary_key=True)
    taller_id = db.Column(db.Integer, primary_key=True)
