from flaskps.db import db


class Genero(db.Model):
    __tablename__ = 'genero'
    id = db.Column(db.Ingeger, primary_key=True)
    nombre = db.Column(db.String)