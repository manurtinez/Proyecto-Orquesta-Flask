from flaskps.db import db
from sqlalchemy import update

class permiso(db.Model):
    __tablename__= 'permiso'

    id = db.Column(db.Integer)
    nombre = db.Column(db.String)

    #Este método sirve para obtener el id de un permiso específico.
    def get_id(nombre_permiso):
        return permiso.query.filter_by(nombre=nombre_permiso).first()