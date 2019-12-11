from flaskps.db import db
from sqlalchemy import update, ForeignKey
from datetime import datetime
import sqlalchemy
from flaskps.models import tipo_instrumento


class Instrumento(db.Model):

    __tablename__ = 'instrumento'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String)
    tipo_id = db.Column(db.Integer,ForeignKey(tipo_instrumento.Tipo_instrumento.id))
    numero_inventario =  db.Column(db.Integer)
    foto =  db.Column(db.String)
    is_deleted = db.Column(db.Boolean)


    #Create (Alta)
    def create(nomb,tid,ni,fo):

        elemento = Instrumento (nombre=nomb,tipo_id=tid,numero_inventario=ni,foto=fo)
        elemento.is_deleted = 0
        db.session.add (elemento)
        db.session.commit()
        return elemento
    
    def logic_delete(i):
        aux = Instrumento.query.filter_by(id=i).first()
        aux.is_deleted = 1
        db.session.commit()
        return aux
    
    def all():
        return Instrumento.query.all()

    def actualizar(i,nom,tid,ni,fo):
        obj = Instrumento.query.filter_by(id=i).first()
        obj.nombre = nom
        obj.numero_inventario = ni
        obj.tipo_id = tid
        obj.foto = fo

        db.session.commit()
        return obj

    def getByID(i):
        return Instrumento.query.filter_by(id=i).first()

    def restaurar(id):
        i = Instrumento.query.filter_by(id=id).first()
        i.is_deleted = 0
        db.session.commit()
        return i

    def notDeletedAll():
        return Instrumento.query.filter_by(is_deleted=0).all()

    def deletedAll():
        return Instrumento.query.filter_by(is_deleted=1).all()
