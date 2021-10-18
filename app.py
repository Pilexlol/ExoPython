from flask import Flask, render_template
from http import HTTPStatus

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", content="Testing")

@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    result = num1 + num2
    return render_template('add.html', num1=num1, num2=num2, result=result)

@app.route('/mul/<int:num1>/<int:num2>')
def mul(num1, num2):
    result = num1 * num2
    return render_template('multiplication.html', num1=num1, num2=num2, result=result)

@app.route('/hello/<name>')
def hello(name):
    #return 'Bonjour {} !'.format(name), HTTPStatus.OK
    return render_template('hello.html', nom=name)