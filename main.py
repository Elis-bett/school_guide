from flask import Flask
from flask import request
from models import School, db
from flask import redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'My_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school1.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/f', methods=['POST'])
def f():
    if request.form['teacher'] != '':
        db.create_all()
        name_teacher = str(request.form['teacher'])
        print(request.form['teacher'])
        cabinets = db.session.query(School.office).filter(School.name == name_teacher).all()
        cabinets1 = ''
        for el in cabinets:
            cabinets1 += " "
            cabinets1 += str(el[0])
        print(cabinets1)
        #print(result)
        return "Вы можете найти учителя в этом кабинете: " + cabinets1
    elif request.form['cabinet'] != '':
        db.create_all()
        office_teacher = str(request.form['cabinet'])
        print(request.form['cabinet'])
        teachers = db.session.query(School.name).filter(School.office == office_teacher).all()
        teachers1 = ''
        for el in teachers:
            teachers1 += " "
            teachers1 += str(el[0])
        print(teachers1)
        return "В этом кабинете вы можете найти: " + teachers1
    return redirect('/')


@app.route('/', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return '''                                                              
            <html>                                                                  
            <head>                                                                  
            </head>                                                                 
            <body>    
            <form action="/f" method="POST">                                                              
            <h1>Здесь вы можете найти кабинет нужного вам учителя</h1>      
            <input type="text" placeholder="Enter name" name="teacher"/>
            <input type="number" placeholder="Enter a number" name="cabinet"/>
            <div class="btn-group">
            <button>поиск по учителю</button>
            <button>поиск по кабинету</button>
            </div>                     
            </body>                                                                 
            </html>                                                                 
            '''
    elif request.method == 'POST':
        print(request.form['teacher'])
        return 'Форма отправлена'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
