from flaskps.db import db
from sqlalchemy import ForeignKey
from flaskps.models import escuela, barrio, nivel

class Estudiante(db.Model):
    __tablename__ = 'estudiante'
    id = db.Column(db.Integer, primary_key=True)
    dni = db.Column(db.Integer)
    localidad_id = db.Column(db.Integer)
    nivel_id = db.Column(db.Integer, ForeignKey(nivel.Nivel.id))
    genero_id = db.Column(db.Integer, ForeignKey(genero.Genero.id))
    escuela_id = db.Column(db.Integer, ForeignKey(escuela.Escuela.id))
    tipo_doc_id = db.Column(db.Integer)
    barrio_id = db.Column(db.Integer, ForeignKey(barrio.Barrio.id))
    apellido = db.Column(db.String)
    nombre = db.Column(db.String)
    domicilio = db.Column(db.String)
    tel = db.Column(db.String)
