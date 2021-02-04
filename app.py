from flask import Flask, jsonify, g
from flask_cors import CORS
from flask_login import LoginManager


import models

#Instantiate app
app = Flask(__name__)

#handle session secret for login_manager before instantiating login manager
app.config.from_pyfile('config.py')

#instantiate LoginManager and initialize in app from app = Flask(__name__)


#allow user to be available anywhere in app

#stub out test route
@app.route('/')
def index():
    return 'hello world'

if __name__=='__main__':
    app.run(port=8000, debug=True)

