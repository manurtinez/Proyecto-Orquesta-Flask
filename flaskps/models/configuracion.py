from flaskps.db import db
from sqlalchemy import update

class configuracion(db.Model):
    __tablename__= 'configuracion'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String)
    descripcion = db.Column(db.String)
    mail = db.Column(db.String)
    cantListar = db.Column(db.Integer)
    sitio_habilitado = db.Column(db.Integer)

    #Consultas para actualización
    def set_titulo(title):
        obj = update(configuracion).where(id=1).\
        values(titulo=title)
        db.session.commit()
        return True

    def set_descripcion(des):
        obj = update(configuracion).where(id=1).\
        values(descripcion=des)
        db.session.commit()
        return True
    
    def set_mail(m):
        obj = update(configuracion).where(id=1).\
        values(mail=m)
        db.session.commit()
        return True

    def set_cantListar(cant):
        obj = update(configuracion).where(id=1).\
        values(cantListar=cant)
        db.session.commit()
        return True
    
    def set_habilitacion(valor):
        # 1 para habilitado. 0 para deshabilitado.
        obj = update(configuracion).where(id=1).\
        values(sitio_habilitado=valor)
        db.session.commit()
        return True
    
    def get_habilitacion():
        return configuracion.query.filter_by(id=1).first()

    def get_config():
        return configuracion.query.filter_by(id=1).first()
    
    def get_titulo():
        return configuracion.query.filter_by(titulo="Orquesta de Berisso").first()