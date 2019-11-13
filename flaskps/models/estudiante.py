from flaskps.db import db
from sqlalchemy import update
from datetime import datetime

class Estudiante(db.Model):
    __tablename__ = 'estudiante'
    id = db.Column(db.Integer, primary_key=True)
    dni = db.Column(db.Integer)
    apellido = db.Column(db.String)
    nombre = db.Column(db.String)
    fecha_nac = db.Column(db.String)
    localidad_id = db.Column(db.Integer)
    nivel_id = db.Column(db.Integer)
    domicilio = db.Column(db.String)
    genero_id = db.Column(db.Integer)
    escuela_id = db.Column(db.Integer)
    tipo_doc_id = db.Column(db.Integer)
    numero = db.Column(db.Integer)
    tel = db.Column(db.String)
    barrio_id = db.Column(db.Integer)

    #Create (Alta)
    def create(dn,ap,no,fe,lo,ni,do,ge,es,ti,nu,te,ba):

        elemento = Estudiante (dni=dn, apellido=ap, nombre=no, fecha_nac=fe, localidad_id=lo, nivel_id=ni, domicilio=do, genero_id=ge, escuela_id=es, tipo_doc_id=ti, numero=nu, tel=te, barrio_id=ba )

        db.session.add (elemento)
        db.session.commit()
        return elemento
        
    #Baja fisica del sistema // SE HACE CON EL DNI
    def eliminar_estudiante(dn):
        Estudiante.query.filter_by(dni=dn).delete()
        db.session.commit()
        return True 

    #ESTA CONSULTA SE ACCEDE CON EL DNI, retorna el objeto actualizado
    def actualizar(dn,ap,no,fe,lo,ni,do,ge,es,ti,nu,te,ba):
        obj = Estudiante.query.filter_by(dni=dn).first()
        obj.apellido = ap
        obj.nombre = no
        obj.fecha_nac = fe
        obj.localidad_id = lo
        obj.nivel_id = ni
        obj.domicilio = do
        obj.genero_id = ge
        obj.escuela_id = es
        obj.tipo_doc_id = ti
        obj.numero = nu
        obj.tel = te
        obj.barrio_id = ba

        db.session.commit()
        return obj

    #Read (devuelve todo)
    def all():
        return Estudiante.query.all()

    

    