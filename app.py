from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from demo_AI!"
    
def subtract(a,b):
    c=(a-b)
    return c
