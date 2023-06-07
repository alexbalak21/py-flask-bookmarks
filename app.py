from flask import Flask, jsonify

app = Flask(__name__)


@app.get('/')
def home():
    return "Home"


@app.get('/hello')
def hello():
    return {'message': 'Hello'}
