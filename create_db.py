from flask import Flask
from models import School, db
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school1.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        artist1 = School(name='Иванов А. С.', office=121)
        artist2 = School(name='Пак М. В.', office=533)
        artist3 = School(name='Третьякова С. А.', office=226)
        artist4 = School(name='Нечаева И. Г.', office=134)
        db.session.add_all([artist1, artist2, artist3, artist4])
        db.session.commit()
