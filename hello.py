from flask import flask

app = Flask(__name__)

@app.route('/')
def hello():
[/t]return 'Hello, World!'
