from flaskps.db import db
from sqlalchemy import update
from datetime import datetime

class Taller(db.Model):
    __tablename__ = 'taller'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String)
    nombre_corto = db.Column(db.String)

    def create(no,nocor):

        elemento = Taller (nombre=no, nombre_corto=nocor)
        db.session.add (elemento)
        db.session.commit()
        return elemento

    def get_by_nombre(nom):
        return Taller.query.filter_by(nombre=nom).first()

    def all():
        return Taller.query.all()

    def get(id):
        return Taller.query.filter_by(id=id).first()

    def serialize(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'nombre_corto': self.nombre_corto,
        }