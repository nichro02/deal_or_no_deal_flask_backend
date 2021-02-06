import models

from flask import Blueprint, jsonify, request
from flask_login import current_user

from playhouse.shortcuts import model_to_dict

#set up blueprint to be used in decorators
games = Blueprint('games', 'games')

#POST ROUTE TO REGISTER GAME RESULTS
@games.route('/', methods=['POST'])
def post_results():
    try:
        payload = request.get_json()
        print(payload)
        game = models.Game.create(**payload)
        game_dict = model_to_dict(game)
        del game_dict['user_id']['password']
        return jsonify(data=game_dict, status={'code': 201, 'message': 'game successfully recorded'})
    except models.DoesNotExist:
        return jsonify(data={}, status={'code': 404, 'message': 'Error getting resources'})
