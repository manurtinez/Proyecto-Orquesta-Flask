from flaskps.db import db
from sqlalchemy import update

class rol(db.Model):
    __tablename__= 'rol'

    id = db.Column(db.Integer)
    nombre = db.Column(db.String)

    #Este método sirve para obtener el id de un rol específico.
    def get_id(nombre_rol):
        return rol.query.filter_by(nombre=nombre_rol).first()
