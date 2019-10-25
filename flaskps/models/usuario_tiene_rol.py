from flaskps.db import db
from sqlalchemy import update

#Ponganle el nombre necesario(?)
class User_tiene_rol(db.Model):
    __tablename__ = 'usuario_tiene_rol'

    usuario_id = db.Column(db.Integer)
    rol_id = db.Column(db.Integer)

    def asignar_rol(usuario_id, rol_id):
        

    def desasignar_rol(usuario_id, rol_id):

    def tiene_rol(usuario_id, rol_id): #ESTE METODO PUEDE USARSE PARA SABER SI EL USUARIO EN CUESTIÓN, 
                                       #TIENE UN DETERMINADO ROL, VALIDAR EL RESULTADO CON NULO EN EL CONTROLADOR.
    