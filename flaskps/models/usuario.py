from flaskps.db import db
from sqlalchemy import update
from datetime import datetime

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

    #agregue esta consulta para chequear si no existe un usuario al registrarse
    def get_by_email(email):
        return User.query.filter_by(email=email).first()

    #esta es para poder buscar por usuario
    def get_by_username(u):
        return User.query.filter(User.username.contains(u)).first()
    
    def all():
        return User.query.all()

    def create(em,us,pa,ac,fi,la):

        elemento = User (email=em, username=us, password=pa, first_name=fi, last_name=la )
        elemento.updated_at= datetime.now()
        elemento.created_at= datetime.now()
        elemento.activo= 1

        db.session.add (elemento)
        db.session.commit()
        return True
     
    #Búsqueda por activo/inactivo
    def select_activos():
        return User.query.filter_by(activo = 1).all()

    def select_inactivos():
        return User.query.filter_by(activo = 0).all()

    #CON ESTE MÉTODO SE PUEDE PEDIR SU ID PARA ASIGNAR ROLES
    def find_by_username(us):
        return User.query.filter_by(username=us).first() 

    #Actualizados
    def activar_user(us):
        obj = User.query.filter_by(username=us).first()
        obj.activo = 1
        db.session.commit()
        return obj

    def desactivar_user(us):
        obj = User.query.filter_by(username=us).first()
        obj.activo = 0
        db.session.commit()
        return obj
    
    #Consultas relacionadas a actualización
    def actualizar_username(usernameviejo,usernamenuevo):
        obj = User.query.filter_by(username=usernameviejo).first()
        obj.username = usernamenuevo
        db.session.commit()
        return True

    def actualizar_password(usern,contraseña):
        obj = User.query.filter_by(username=usern).first()
        obj.password = contraseña
        db.session.commit()
        return True

    #ESTA CONSULTA SE ACCEDE CON EL NOMBRE DE USUARIO (viejo), RETORNA EL OBJETO ACTUALIZADO
    def actualizar(useractual,usernuevo,passnueva,firnuevo,lanuevo):
        obj = User.query.filter_by(username=useractual).first()
        obj.username = usernuevo
        obj.password = passnueva
        obj.first_name = firnuevo
        obj.last_name = lanuevo
        obj.updated_at = datetime.now()
        db.session.commit()
        return obj

    #Baja fisica del sistema
    def eliminar_usuario(email):
        User.query.filter_by(email=email).delete()
        db.session.commit()
        return True 

#por cada metodo va su equivalente en el controlador, ahi aseguro q no este vacio. redirigir desde el mismo controlador.