from flaskps.db import db
from flaskps.models.rol import Rol
from flaskps.models.permiso import Permiso
from sqlalchemy import update, ForeignKey, PrimaryKeyConstraint

class rol_tiene_permiso(db.Model):
    __tablename__= 'rol_tiene_permiso'
    __table_args__ = (
        PrimaryKeyConstraint('id_rol', 'id_permiso'),
    )

    id_rol = db.Column(db.Integer,ForeignKey(Rol.id))
    id_permiso = db.Column(db.Integer,ForeignKey(Permiso.id))
    
    # Con este método, se sabe si un rol tiene un permiso específico. Se debe utilizar pasándole los id de ambas cosas 
    #   (para ello ambas clases poseen un método para averiguarlo)
    def tiene_permiso(idrol,idpermiso):
        return Permiso.query.filter_by(id_rol=idrol, id_permiso=idpermiso).first()

    def all():
        return rol_tiene_permiso.query.all()