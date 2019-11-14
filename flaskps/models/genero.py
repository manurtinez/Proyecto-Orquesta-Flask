from flaskps.db import db


class Genero(db.Model):
    __tablename__ = 'genero'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String)

    def get_all():
        return Genero.query.all()