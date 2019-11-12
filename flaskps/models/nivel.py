from flaskps.db import db

class Nivel(db.Model):
    __tablename__ = 'nivel'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String)

    def get_all():
        return Nivel.query.all()