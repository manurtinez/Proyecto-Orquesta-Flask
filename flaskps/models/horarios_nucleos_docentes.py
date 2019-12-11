from flaskps.db import db
from sqlalchemy import ForeignKey, PrimaryKeyConstraint
from flaskps.models import docente, taller, ciclo_lectivo, nucleo

class Horarios_Nucleos_Docentes(db.Model):
    __tablename__ = 'horarios_nucleos_docentes'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    docente_id = db.Column(db.Integer, ForeignKey(docente.Docente.id))
    ciclo_lectivo_id = db.Column(db.Integer, ForeignKey(ciclo_lectivo.Ciclo_lectivo.id))
    taller_id = db.Column(db.Integer, ForeignKey(taller.Taller.id))
    nucleo_id = db.Column(db.Integer, ForeignKey(nucleo.Nucleo.id))
    dia = db.Column(db.String)

    def all():
        return Horarios_Nucleos_Docentes.query.all()

    def create(do,ci,ta, nid, dia):
        elemento = Horarios_Nucleos_Docentes (docente_id=do, ciclo_lectivo_id=ci, taller_id=ta, nucleo_id=nid, dia=dia)
        db.session.add (elemento)
        db.session.commit()
        return elemento

    def getByID(id):
        return Horarios_Nucleos_Docentes.query.filter_by(id=id).first()

    def getByInfo(do, ci, ta, nid, dia):
        return Horarios_Nucleos_Docentes.query.filter_by(docente_id=do, ciclo_lectivo_id=ci, taller_id=ta, nucleo_id=nid, dia=dia).first()
        
    def delete(id):
        elemento = Horarios_Nucleos_Docentes.query.filter_by(id=id).first()
        db.session.delete(elemento)
        db.session.commit()