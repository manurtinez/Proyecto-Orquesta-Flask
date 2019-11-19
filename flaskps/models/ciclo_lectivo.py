from flaskps.db import db
from sqlalchemy import update
from datetime import datetime
from sqlalchemy.orm import relationship

class Ciclo_lectivo(db.Model):

    __tablename__ = 'ciclo_lectivo'
    id = db.Column(db.Integer, primary_key=True)
    fecha_ini = db.Column(db.String)
    fecha_fin = db.Column(db.String)
    semestre = db.Column(db.Integer)
    children = relationship('Ciclo_lectivo_taller', cascade='all, delete',
    backref='ciclo_lectivo')

    #Añadir un ciclo lectivo
    def create(ini,fin,se):
        elemento = Ciclo_lectivo (fecha_ini=ini, fecha_fin=fin, semestre=se)

        db.session.add (elemento)
        db.session.commit()
        return elemento
    
    #Baja fisica del sistema // SE HACE CON FECHA DE INICIO
    def eliminar_ciclolectivo(i):
        c = Ciclo_lectivo.query.filter_by(id=i).first()
        db.session.delete(c)
        db.session.commit()
        return True 
    
    #ESTA CONSULTA SE ACCEDE CON EL id, retorna el objeto actualizado
    def actualizar(i,fi,ff,sem):
        obj = Ciclo_lectivo.query.filter_by(id=i).first()
        obj.fecha_ini = fi
        obj.fecha_fin = ff
        obj.semestre = sem

        db.session.commit()
        return obj
    
    #Read (devuelve todo)
    def all():
        return Ciclo_lectivo.query.all()
    