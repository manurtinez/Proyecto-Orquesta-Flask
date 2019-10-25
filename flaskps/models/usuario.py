from flaskps.db import db
from sqlalchemy import update

class User(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)
    username = db.Column(db.String)
    password = db.Column(db.String)
    activo = db.Column(db.Integer)
    updated_at = db.Column(db.String)
    created_at = db.Column(db.String)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    

    def get_by_id(id):
        return User.query.get(id)

    def get_by_email_and_pass(email, password):
        return User.query.filter_by(email=email, password=password).first()

    def all():
        return User.query.all()

    def create(em,us,pa,ac,up,cr,fi,la):

        elemento = usuario (email=em, username=us, password=pa, activo=ac, updated_at=up, 
        created_at=cr, first_name=fi, last_name=la )

        dbsession.add (elemento)
        dbsession.flush() #probar este modulo T^T   
        return True
     
    def select_activos():
        return User.query.filter_by(activo = 1).all()

    def find_by_username(us):
        return User.query.filter_by(username=us).first()  #CON ESTE MÉTODO SE PUEDE PEDIR SU ID PARA ASIGNAR ROLES

    def activar_user(us):
        obj = update(usuario).where(username=us).\
        values(activo='1')
        return True

    def desactivar_user(us):
        obj = update(usuario).where(username=us).\
        values (activo= '0')
        return True

#por cada metodo va su equivalente en el controlador, ahi aseguro q no este vacio. redirigir desde el mismo controlador.