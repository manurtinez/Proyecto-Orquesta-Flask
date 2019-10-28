from flaskps.db import db
from sqlalchemy import update

class rol_tiene_permiso(db.Model):
    __tablename__= 'rol_tiene_permiso'

    id_rol = db.Column(db.Integer)
    id_permiso = db.Column(db.Integer)
    
    # Con este método, se sabe si un rol tiene un permiso específico. Se debe utilizar pasándole los id de ambas cosas 
    #   (para ello ambas clases poseen un método para averiguarlo)
    def rol_tiene_permiso(idrol,idpermiso):
        return permiso.query.filter_by(id_rol=idrol, id_permiso=idpermiso).first()