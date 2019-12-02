from flaskps.db import db
from sqlalchemy import update

class Responsable(db.Model):
    __tablename__ = 'responsable'

    id = db.Column(db.Integer, primary_key=True)
    apellido = db.Column(db.String)
    nombre = db.Column(db.String)
    domicilio = db.Column(db.String)
    tel = db.Column(db.String)
    fecha_nac = db.Column(db.Date)
    localidad_id = db.Column(db.Integer)
    genero_id = db.Column(db.Integer)
    tipo_doc_id = db.Column(db.Integer)
    numero = db.Column(db.Integer)
    is_deleted = db.Column(db.Boolean)

    def all():
        return Responsable.query.all()

    def getById(id):
        return Responsable.query.filter_by(id=id).first()

    def create(ap,no,fe,lo,do,ge,ti,nu,te):
        elemento = Responsable (apellido=ap, nombre=no, fecha_nac=fe, localidad_id=lo, domicilio=do, genero_id=ge, tipo_doc_id=ti, numero=nu, tel=te)
        elemento.is_deleted = 0
        db.session.add (elemento)
        db.session.commit()
        return elemento