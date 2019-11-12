from flaskps.db import db
from sqlalchemy import update

class Escuela(db.Model):
    __tablename__='escuela'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String)
    direccion = db.Column(db.String)
    telefono = db.Column(db.String)

    def get_all():
        return Escuela.query.all()

    def get_by_id(id):
        return Escuela.query.get(id)