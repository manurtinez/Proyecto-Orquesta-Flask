from flaskps.db import db
from sqlalchemy import update
import sqlalchemy

class Tipo_instrumento(db.Model):

    __tablename__ = 'tipo_instrumento'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String)

    def all():
        return Tipo_instrumento.query.all()

    def getByID(i):
        return Tipo_instrumento.query.filter_by(id=i).first()
    
