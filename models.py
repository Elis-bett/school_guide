from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class School(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    office = db.Column(db.Integer, unique=True, nullable=True)

    def __init__(self, name, office):
        self.name = name
        self.office = office

    def __repr__(self):
        return '<School %r: %r>' % (self.name, self.name)
