from flaskps.db import db

class Barrio(db.Model):
    __tablename__ = 'barrio'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String)

    def get_all():
        return Barrio.query.all()