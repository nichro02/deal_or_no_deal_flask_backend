import os

from flask import Flask, jsonify, g
from flask_cors import CORS
from flask_login import LoginManager

from resources.players import players
from resources.games import games
from resources.comments import comments

import models

#Instantiate app
app = Flask(__name__)

#handle session secret for login_manager before instantiating login manager
app.config.from_pyfile('/app/config.py')

#instantiate LoginManager and initialize in app from app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)

#allow user to be available anywhere in app
@login_manager.user_loader
def load_user(player_id):
    try:
        return models.Player.get_by_id(player_id)
    except models.DoesNotExist:
        return None

@app.before_request
def before_request():
    """Connect to the database before each request"""
    g.db = models.DATABASE
    g.db.connect()

@app.after_request
def after_request(response):
    """Close database connection after each request"""
    g.db.close()
    return response

CORS(app, origins=['http://localhost:3000','https://fierce-lake-32005.herokuapp.com/'], supports_credentials=True)

app.register_blueprint(players, url_prefix='/api/v1/players')
app.register_blueprint(games, url_prefix='/api/v1/games')
app.register_blueprint(comments, url_prefix='/api/v1/comments')


#stub out test route
@app.route('/')
def index():
    return 'hello world'

if 'ON_HEROKU' in os.environ:
    print('hitting')
    models.initialize()

if __name__=='__main__':
    models.initialize()
    app.run(debug=True)

