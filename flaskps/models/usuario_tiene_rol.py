from flaskps.db import db
from sqlalchemy import update

#Ponganle el nombre necesario(?)
class User_tiene_rol(db.Model):
    __tablename__ = 'usuario_tiene_rol'

    usuario_id = db.Column(db.Integer)
    rol_id = db.Column(db.Integer)

    def asignar_rol(idusuario, idrol):
        #agrega tupla a la tabla
        elemento = usuario_tiene_rol (usuario_id = idusuario, rol_id = idrol)
        dbsession.add (elemento)
        db.session.commit()   
        return True


    def desasignar_rol(uid, rid):
        #borra tupla de la tabla
        User_tiene_rol.query.filter_by(usuario_id=uid, rol_id=rid).delete()
        db.session.commit()
        return True 

    # El siguiente método se usa con los id's, para ello cada clase tiene un método por el cual
    #   pueden obtenerse.
    def tiene_rol(uid, rid): #ESTE METODO PUEDE USARSE PARA SABER SI EL USUARIO EN CUESTIÓN, 
                             #TIENE UN DETERMINADO ROL, VALIDAR EL RESULTADO CON NULO EN EL CONTROLADOR (comparar con none)
    return User_tiene_rol.query.filter_by(usuario_id=uid, rol_id=rid).first()