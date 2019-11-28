from flaskps.db import db
from sqlalchemy import update, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from flaskps.models import escuela, barrio, nivel, genero

class Estudiante(db.Model):
    __tablename__ = 'estudiante'
    id = db.Column(db.Integer, primary_key=True)
    apellido = db.Column(db.String)
    nombre = db.Column(db.String)
    fecha_nac = db.Column(db.String)
    localidad_id = db.Column(db.Integer)
    nivel_id = db.Column(db.Integer, ForeignKey(nivel.Nivel.id))
    domicilio = db.Column(db.String)
    genero_id = db.Column(db.Integer, ForeignKey(genero.Genero.id))
    escuela_id = db.Column(db.Integer, ForeignKey(escuela.Escuela.id))
    tipo_doc_id = db.Column(db.Integer)
    numero = db.Column(db.Integer) #DNI
    tel = db.Column(db.String)
    barrio_id = db.Column(db.Integer, ForeignKey(barrio.Barrio.id))
    is_deleted = db.Column(db.Boolean)
    estudiante_taller = relationship('Estudiante_taller', cascade='all, delete',
    backref='estudiante')

    #Create (Alta)
    def create(ap,no,fe,lo,ni,do,ge,es,ti,nu,te,ba):

        elemento = Estudiante (apellido=ap, nombre=no, fecha_nac=fe, localidad_id=lo, nivel_id=ni, domicilio=do, genero_id=ge, escuela_id=es, tipo_doc_id=ti, numero=nu, tel=te, barrio_id=ba )
        elemento.is_deleted = 0
        db.session.add (elemento)
        db.session.commit()
        return elemento
    
    #Verificar si un DNI existe en el sistema (si no existe retorna nulo)
    def getByDNI(dni):
        return Estudiante.query.filter_by(numero=dni).first()
        
    #Baja fisica del sistema // SE HACE CON EL DNI
    def eliminar_estudiante(dn):
        e = Estudiante.query.filter_by(numero=dn).first()
        db.session.delete(e)
        db.session.commit()
        return True 

    #ESTA CONSULTA SE ACCEDE CON EL DNI VIEJO, retorna el objeto actualizado
    def actualizar(nuVIEJO,ap,no,fe,lo,ni,do,ge,es,ti,te,ba):
        obj = Estudiante.query.filter_by(numero=nuVIEJO).first()
        obj.apellido = ap
        obj.nombre = no
        obj.fecha_nac = fe
        obj.localidad_id = lo
        obj.nivel_id = ni
        obj.domicilio = do
        obj.genero_id = ge
        obj.escuela_id = es
        obj.tipo_doc_id = ti
        obj.tel = te
        obj.barrio_id = ba

        db.session.commit()
        return obj

    #Read (devuelve todo)
    def all():
        return Estudiante.query.all()

    def logic_delete(dni):
        e = Estudiante.query.filter_by(numero=dni).first()
        e.is_deleted = 1
        db.session.commit()
        return e

    def notDeletedAll():
        return Estudiante.query.filter_by(is_deleted=0).all()

    def deletedAll():
        return Estudiante.query.filter_by(is_deleted=1).all()

    def restaurar(id):
        e = Estudiante.query.filter_by(id=id).first()
        e.is_deleted = 0
        db.session.commit()
        return e
