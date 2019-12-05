from flaskps.db import db
from sqlalchemy import update
from datetime import datetime
from sqlalchemy.orm import relationship
import sqlalchemy

class Ciclo_lectivo(db.Model):

    __tablename__ = 'ciclo_lectivo'
    id = db.Column(db.Integer, primary_key=True)
    fecha_ini = db.Column(db.String)
    fecha_fin = db.Column(db.String)
    semestre = db.Column(db.Integer)
    ciclo_lectivo_taller = relationship('Ciclo_lectivo_taller', cascade='all, delete',
    backref='ciclo_lectivo')
    docente_responsable_taller = relationship('Docente_responsable_taller', cascade='all, delete',
    backref='ciclo_lectivo')
    estudiante_taller = relationship('Estudiante_taller', cascade='all, delete',
    backref='ciclo_lectivo')

    def serialize(self):
        return {
            'fecha_ini': self.fecha_ini,
            'fecha_fin': self.fecha_fin,
            'semestre': self.semestre,
        }

    def getByYear(an):
        #act = datetime(datetime.today().year, datetime.today().month, datetime.today().day)
        return Ciclo_lectivo.query.filter(sqlalchemy.extract('year', Ciclo_lectivo.fecha_ini)== an).all()
        #fecha_ini.year()
        #c = Ciclo_lectivo.query.filter_by(semestre=sem, fecha_ini=an).first()

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

    
    def get(fi, fin, sem):
        return Ciclo_lectivo.query.filter_by(fecha_ini=fi, fecha_fin=fin, semestre=sem).first()

    def getByid(cid):
        return Ciclo_lectivo.query.filter_by(id=cid).first()