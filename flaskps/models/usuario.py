from flaskps.db import db
from sqlalchemy import update

class User(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)
    password = db.Column(db.String)
    def get_by_id(id):
        return User.query.get(id)

    def get_by_email_and_pass(email, password):
        return User.query.filter_by(email=email, password=password).first()

    def all():
        return User.query.all()

    def create(em,us,pa,ac,up,cr,fi,la)

        elemento = Usuario (email=em, username=us, password=pa, activo=ac, updated_at=up, 
        created_at=cr, first_name=fi, last_name=la )
        return True
    
    def select_activos():
        return User.query.filter_by(activo = 1).all()

    def find_by_username(us):
        return User.query.filter_by(username=us).first()

    def activar_user(us):
        obj = update(usuario).where(username=us).\
        values(activo='1')
        return True



#     @classmethod
#     def activar_user(cls,username):
#         sql= "UPDATE usuario SET activo = 1 WHERE usuario.username = @username "

#         cursor = cls.db.cursor()
#         cursor.execute(sql)
#         return True

#     @classmethod
#     def desactivar_user(cls,username):
#         sql= "UPDATE usuario SET activo = 0 WHERE usuario.username = @username "

#         cursor = cls.db.cursor()
#         cursor.execute(sql)
#         return True

# >>>>HACER ASIGNACIÓN DE ROLES

# #por cada metodo va su equivalente en el controlador, ahi aseguro q no este vacio. redirigir desde el mismo controlador.