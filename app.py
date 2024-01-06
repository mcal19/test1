from flask import Flask
import g4f
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!' + str(g4f)
