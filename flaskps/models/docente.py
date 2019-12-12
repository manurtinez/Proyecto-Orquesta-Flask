from flaskps.db import db
from sqlalchemy import update
from sqlalchemy.orm import relationship
from datetime import datetime

class Docente(db.Model):
    __tablename__ = 'docente'
    id = db.Column(db.Integer, primary_key=True)
    apellido = db.Column(db.String)
    nombre = db.Column(db.String)
    fecha_nac = db.Column(db.String)
    localidad_id = db.Column(db.Integer)
    domicilio = db.Column(db.String)
    genero_id = db.Column(db.Integer)
    tipo_doc_id = db.Column(db.Integer)
    numero = db.Column(db.Integer) #DNI
    tel = db.Column(db.String)
    is_deleted = db.Column(db.Boolean)
    docente_responsable_taller = relationship('Docente_responsable_taller', cascade='all, delete',
    backref='docente')

    #Read (devuelve todo)
    def all():
        return Docente.query.all()

    def get(id):
        return Docente.query.filter_by(id=id).first()

    #Verifica si un DNI existe en el sistema (si no existe retorna nulo)
    def getByDNI(num):
        return Docente.query.filter_by(numero=num).first()
        
    #Baja fisica del sistema // SE HACE CON EL DNI
    def eliminar_docente(dn):
        d = Docente.query.filter_by(numero=dn).first()
        db.session.delete(d)
        db.session.commit()
        return True 

    #Alta
    def create(ap,no,fe,lo,do,ge,ti,nu,te):
        elemento = Docente (apellido=ap, nombre=no, fecha_nac=fe, localidad_id=lo, domicilio=do, genero_id=ge, tipo_doc_id=ti, numero=nu, tel=te)
        elemento.is_deleted = 0
        db.session.add (elemento)
        db.session.commit()
        return elemento

    #ESTA CONSULTA SE ACCEDE CON EL DNI VIEJO, retorna el objeto actualizado
    def actualizar(nuVIEJO,ap,no,fe,lo,do,ge,ti,te):
        obj = Docente.query.filter_by(numero=nuVIEJO).first()
        obj.apellido = ap
        obj.nombre = no
        obj.fecha_nac = fe
        obj.localidad_id = lo
        obj.domicilio = do
        obj.genero_id = ge
        obj.tipo_doc_id = ti
        obj.tel = te

        db.session.commit()
        return obj

    def logic_delete(dni):
        d = Docente.query.filter_by(numero=dni).first()
        d.is_deleted = 1
        db.session.commit()
        return d

    def notDeletedAll():
        return Docente.query.filter_by(is_deleted=0).all()

    def deletedAll():
        return Docente.query.filter_by(is_deleted=1).all()

    def restaurar(id):
        d = Docente.query.filter_by(id=id).first()
        d.is_deleted = 0
        db.session.commit()
        return d