# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, CI/CD!"

@app.route('/status')
def status():
    return "Application is running!"

if __name__ == "_main_":
    app.run()