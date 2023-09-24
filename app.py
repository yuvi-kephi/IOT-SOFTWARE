from flask import Flask, render_template, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db = SQLAlchemy()

from models import *

db.init_app(app=app)
with app.app_context():
    db.create_all()

my_data = {
    'count': "",
    'humidity':1,
    'ec': 36.9,
    'ph': 6.71,
    'turbidity': 20.34,
    'tds': 0,
    'temp': 0.04,
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Check if the username and password are valid
    if username == 'KEPHICTO' and password == 'kipl@18':
        return redirect('/loggedin')
    elif username == 'KEPHICEO' and password == 'kipl@18':
        return redirect('/loggedin')
    elif username == 'KEPHIMD' and password == 'kipl@18':
        return redirect('/loggedin')
    else:
        return redirect('/failure')

@app.route('/send-data', methods=["POST"])
def send_data():
    global my_data
    if request.method=="POST":
        my_data['count'] = request.get_json()['count']
        my_data['humidity'] = request.get_json()['Humidity']
        my_data['ec'] = request.get_json()['ec']
        my_data['ph'] = request.get_json()['ph']
        my_data['turbidity'] = request.get_json()['turbidity']
        my_data['tds'] = request.get_json()['tds']
        my_data['temp'] = request.get_json()['temp']
    
    print(my_data)

    d = Data(
        count = my_data['count'],
        humidity = my_data['humidity'],
        ec = my_data['ec'],
        ph = my_data['ph'],
        turbidity = my_data['turbidity'],
        tds = my_data['tds'],
        temperature = my_data['temp']
    )

    db.session.add(d)
    db.session.commit()

    return jsonify({'status':'OK'})

@app.route('/get-data')
def get_data():
    global my_data
    #try:
    #    d = Data.query.all()[30:]
    #except:
    #    d = Data.query.all()
    #print(d)
    print("...............",my_data)
    return jsonify({'data':render_template('update_chart.html',data=my_data)})

@app.route('/loggedin')
def loggedin():
    global my_data
    try:
        d = Data.query.all()[30:]
    except:
        d = Data.query.all()
    data_ = [[i.temperature,i.ph, i.ec, i.tds, i.turbidity,i.humidity] for i in d]
    return render_template('userinterface.html', data=my_data)

@app.route('/failure')
def failure():
    return 'Incorrect Username or Password!'

if __name__ == '__main__':
    app.run(debug=True, port=8000)
