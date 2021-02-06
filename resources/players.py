import models

from flask import Blueprint, jsonify, request
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, current_user

from playhouse.shortcuts import model_to_dict

#set up blueprint to be used in decorators
players = Blueprint('players', 'players')

#POST ROUTE TO REGISTER PLAYERS
@players.route('/register', methods=['POST'])
def register():
    payload = request.get_json()
    payload['email'].lower()

    #check to see if user already exists/username is taken
    try:
        models.Player.get(models.Player.email == payload['email'])
        return jsonify(data={}, status={'code': 401, 'message': 'user with email already exists'})
    except models.DoesNotExist:
        #if user does not exist, create user
        payload['password'] = generate_password_hash(payload['password'])
        player = models.Player.create(**payload)

        login_user(player)

        player_dict = model_to_dict(player)

        #check player_dict
        print('BEFORE ---->', player_dict)
        #delete password key from player_dict
        del player_dict['password']
        #check deletion
        print('AFTER ---->', player_dict)

        return jsonify(data=player_dict, status={'code': 201, 'message': 'user created'})

#POST ROUTE TO LOGIN PLAYERS

#PUT ROUTE TO UPDATE BIO

#GET, POST ROUTE TO LOGOUT PLAYERS

#DELETE PLAYER