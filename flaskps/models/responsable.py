from flaskps.db import db
from sqlalchemy import update

class Responsable(db.Model):
    __tablename__ = 'responsable'

    id = db.Column(db.Integer, primary_key=True)
    apellido = db.Column(db.String)
    nombre = db.Column(db.String)
    domicilio = db.Column(db.String)
    tel = db.Column(db.String)
    fecha_nac = db.Column(db.Date)
    localidad_id = db.Column(db.Integer)
    genero_id = db.Column(db.Integer)
    tipo_doc_id = db.Column(db.Integer)
    numero = db.Column(db.Integer)

    def all():
        return Responsable.query.all()

    def getById(id):
        return Responsable.query.filter_by(id=id).first()