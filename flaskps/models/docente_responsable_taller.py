from flaskps.db import db
from sqlalchemy import update
from datetime import datetime

class Docente_responsable_taller(db.Model):
    __tablename__ = 'ciclo_lectivo_taller'
    docente_id = db.Column(db.Integer, primary_key=True)
    ciclo_lectivo_id = db.Column(db.Integer, primary_key=True)
    taller_id = db.Column(db.Integer, primary_key=True)

    #Se crea con un solo docente, para agregar mas de uno, usar el metodo abajo del create.
    def create(do,ci,ta):
        elemento = Docente_responsable_taller (docente_id=do, ciclo_lectivo_id=ci, taller_id=ta)

        db.session.add (elemento)
        db.session.commit()
        return elemento
    
    # Para agregar con 2 docentes (comparás en el form con nulo, si no es nulo en el form el segundo campo
    # de docentes, entonces ahí usas este, es exactamente igual pero con un parametro mas.)
    # Para este los parámetros son (id_docente_1°, id_docente_2°, ciclo, taller)
    def create(do,do2,ci,ta):
        elemento = Docente_responsable_taller (docente_id=do, ciclo_lectivo_id=ci, taller_id=ta)
        db.session.add (elemento)
        elemento2 = Docente_responsable_taller (docente_id=do2, ciclo_lectivo_id=ci, taller_id=ta)
        db.session.add (elemento2)
        db.session.commit()
        return elemento

    # Lo mismo pero para 3 docentes, traté de hacerlo lo mas fácil posible para no mezclar mil tablas
    # en la consulta (?) 
    # Y yo digo que máximo van a ser 3 docentes, jaja salu2
    def create(do,do2,do3,ci,ta):
        elemento = Docente_responsable_taller (docente_id=do, ciclo_lectivo_id=ci, taller_id=ta)
        db.session.add (elemento)
        elemento2 = Docente_responsable_taller (docente_id=do2, ciclo_lectivo_id=ci, taller_id=ta)
        db.session.add (elemento2)
        elemento3 = Docente_responsable_taller (docente_id=do3, ciclo_lectivo_id=ci, taller_id=ta)
        db.session.add (elemento3)
        db.session.commit()
        return elemento