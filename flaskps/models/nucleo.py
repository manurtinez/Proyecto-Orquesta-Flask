from flaskps.db import db

class Nucleo(db.Model):
    __tablename__ = 'nucleo'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String)

    def get_all():
        return Nucleo.query.all()

    def get_by_nombre(nombre_nucleo):
        return Nucleo.query.filter_by(nombre=nombre_nucleo).first()

    def get_by_id(unid):
        return Nucleo.query.filter_by(id=unid).first()