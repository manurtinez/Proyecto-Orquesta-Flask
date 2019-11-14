from flaskps.db import db
from sqlalchemy import update
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

    #Read (devuelve todo)
    def all():
        return Docente.query.all()

    #Verifica si un DNI existe en el sistema (si no existe retorna nulo)
    def existe_dni(num):
        elem = Docente.query.filter_by(numero=num).first()
        return elem
        
    #Baja fisica del sistema // SE HACE CON EL DNI
    def eliminar_docente(dn):
        Docente.query.filter_by(numero=dn).delete()
        db.session.commit()
        return True 

    #Alta
    def create(ap,no,fe,lo,do,ge,ti,nu,te):
        elemento = Docente (apellido=ap, nombre=no, fecha_nac=fe, localidad_id=lo, domicilio=do, genero_id=ge, tipo_doc_id=ti, numero=nu, tel=te)

        db.session.add (elemento)
        db.session.commit()
        return elemento

    #ESTA CONSULTA SE ACCEDE CON EL DNI VIEJO, retorna el objeto actualizado
    def actualizar(nuVIEJO,ap,no,fe,lo,do,ge,ti,nuNUEVO,te):
        obj = Docente.query.filter_by(numero=nuVIEJO).first()
        obj.apellido = ap
        obj.nombre = no
        obj.fecha_nac = fe
        obj.localidad_id = lo
        obj.domicilio = do
        obj.genero_id = ge
        obj.tipo_doc_id = ti
        obj.numero = nuNUEVO
        obj.tel = te

        db.session.commit()
        return obj