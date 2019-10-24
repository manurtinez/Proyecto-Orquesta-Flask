from flaskps.db import db

class User(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)
    password = db.Column(db.String)
    def get_by_id(id):
        return User.query.get(id)
    def get_by_email_and_pass(email, password):
        return User.query.filter_by(email=email, password=password).first()
#     db = None

#     @classmethod
#     def all(cls):
#         sql = "SELECT * FROM usuario"

#         cursor = cls.db.cursor()
#         cursor.execute(sql)

#         return cursor.fetchall()

#     @classmethod
#     def create(cls, em, us, pa, ac, up, cr, fi, la): #1° no esten vacios (verificar desde el controlador, resources > usuario.py).
#         sql = """
#             INSERT INTO usuario (email, username, password, activo, updated_at, created_at, first_name, last_name )
#             VALUES (@em, @us, @pa, @ac, @up, @cr, @fi, @la) 
#         """
#         cursor = cls.db.cursor()
#         cursor.execute(sql)
#         cls.db.commit()

#         return True

#     @classmethod
#     def select_activos(cls):
#         sql = "SELECT * FROM usuario WHERE usuario.activo = 1"

#         cursor = cls.db.cursor()
#         cursor.execute(sql)

#         return cursor.fetchall()

#     @classmethod
#     def find_by_email_and_pass(cls,e,p):
#         sql = "SELECT * FROM usuario WHERE usuario.email = @e AND usuario.password = @p" 
#         #asegurar que compare con las variables, no con el string

#         cursor = cls.db.cursor()
#         resultado = cursor.execute(sql) 
#         return resultado

#     @classmethod
#     def find_by_username(cls, username):
#         sql = "SELECT * FROM usuario WHERE usuario.username = @username"
#         cursor = cls.db.cursor()
#         resultado = cursor.execute(sql)
#         return resultado

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


# #por cada metodo va su equivalente en el controlador, ahi aseguro q no este vacio. redirigir desde el mismo controlador.