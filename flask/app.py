from flask import Flask, render_template, request
from markupsafe import escape
from functools import reduce

app = Flask(__name__)

@app.route('/add/<numbers>')
def add(numbers):
    numbers = list(map(int, numbers.split(',')))
    return f'{sum(numbers)}'

@app.route('/sub/<numbers>')
def sub(numbers):
    numbers = list(map(int, numbers.split(',')))
    return f'{reduce(lambda x, y: x - y, numbers)}'

@app.route('/mul/<numbers>')
def mul(numbers):
    numbers = list(map(int, numbers.split(',')))
    return f'{reduce(lambda x, y: x * y, numbers)}'

@app.route('/div/<numbers>')
def div(numbers):
    numbers = list(map(int, numbers.split(',')))
    return f'{reduce(lambda x, y: x / y, numbers)}'

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)