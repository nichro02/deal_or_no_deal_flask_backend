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
@players.route('/login', methods=['POST'])
def login():
    payload = request.get_json()
    #payload['username'].lower()

    try:
        #check email
        player = models.Player.get(models.Player.username == payload['username'])
        print('USER --->', player)

        player_dict = model_to_dict(player)

        #check password
        if(check_password_hash(player_dict['password'], payload['password'])):
            del player_dict['password']
            #start session if password is correct
            login_user(player)
            return jsonify(data=player_dict, status={'code': 200, 'message': 'successful login'})
        else:
            #send incorrect login info message
            return jsonify(data={}, status={'code': 401, 'message': 'incorrect login information provided'})
    except models.DoesNotExist:
        return jsonify(data={}, status={'code': 401, 'message': 'incorrect login information provided'})

#GET, POST ROUTE TO LOGOUT PLAYERS
@players.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return jsonify(data={}, status={'code': 200, 'message': 'logout successful'})

#GET ROUTE TO RETRIEVE ONE USER
@players.route('/<player_id>', methods=['GET'])
def get_one_player(player_id):

    try:
        #retrieve player
        get_player = models.Player.get_by_id(player_id)
        player_dict = model_to_dict(get_player)
        del player_dict['password']
        #breakpoint()
        #retrieve player's games
        query = models.Game.select(models.Game.id, models.Game.score, models.Game.timestamp).join(models.Player).where(models.Game.user_id == player_id)
        query_dict = [model_to_dict(q) for q in query]
        for item in query_dict:
            del item['user_id']
        #query = get_player.join(models.Game, on=(models.Game.user_id == models.Player.id))
        return jsonify(data={'player': player_dict,'games': query_dict}, status={'code': 200, 'message':'player retrieved'})
    except models.DoesNotExist:
        return jsonify(data={}, status={'code': 401, 'message': 'error retrieving resources'})

#PUT ROUTE TO UPDATE BIO
@players.route('/<player_id>', methods=['PUT', 'OPTIONS'])
def update_bio(player_id):
    try:
        payload = request.get_json()
        query = models.Player.update(**payload).where(models.Player.id==player_id)
        query.execute()
        updated_player = model_to_dict(models.Player.get_by_id(player_id))
        del updated_player['password']
        return jsonify(data=updated_player, status={'code': 200, 'message': 'User successfully updated'})
    except models.DoesNotExist:
        return jsonify(data={}, status={'code': 404,'message': 'Error getting resources'})

#DELETE PLAYER
@players.route('/<player_id>', methods=['Delete'])
def delete_player(player_id):
    try:
        player_to_delete = models.Player.get_by_id(player_id)
        player_to_delete.delete_instance()
        return jsonify(data={}, status={'code': 200, 'message': 'Record successfully deleted'})
    except models.DoesNotExist:
        return jsonify(data={}, status={'code': 404,'message': 'Error getting resources'})