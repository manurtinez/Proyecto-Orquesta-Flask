from flaskps.db import db
from sqlalchemy import update

class Permiso(db.Model):
    __tablename__= 'permiso'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String)

    #Este método sirve para obtener el id de un permiso específico.
    def get_id(nombre_permiso):
        return Permiso.query.filter_by(nombre=nombre_permiso).first()

    def all():
        return Permiso.query.all()