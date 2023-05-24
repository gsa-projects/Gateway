from flask import Flask, render_template, current_app
from os import path
from sqlalchemy import create_engine,text
import json

with open(path.join(path.dirname(__file__), 'config.json'), 'r') as config:
    configs = json.load(config)
    DB_URL = f"mysql+mysqlconnector://{configs['user']}:{configs['password']}@{configs['host']}:{configs['port']}/{configs['database']}?charset=utf8"

def do(sqltext):
    with current_app.database.connect() as connection:
        result = connection.execute(text(sqltext))
        return result

app = Flask(__name__)
app.config.from_file('config.json', load=json.load)
database = create_engine(DB_URL, max_overflow=0)
app.database = database

@app.route('/')
def index():
    column_names = [column[0] for column in do("DESCRIBE actor;")]
    data = [*do("SELECT * FROM actor LIMIT 50")]

    return render_template('index.html', column_names=column_names, data=data)

if __name__ == '__main__':
    app.run(debug=True)