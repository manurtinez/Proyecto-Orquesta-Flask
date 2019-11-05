from flaskps.db import db
from sqlalchemy import update

class Rol(db.Model):
    __tablename__= 'rol'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String)

    #Este método sirve para obtener el id de un rol específico.
    def get_by_nombre(nombre_rol):
        return Rol.query.filter_by(nombre=nombre_rol).first()

    def all():
        return Rol.query.all()
