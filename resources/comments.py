import models

from flask import Blueprint, jsonify, request
from flask_login import current_user

from playhouse.shortcuts import model_to_dict

#set up blueprint to be used in decorators
comments = Blueprint('comments', 'comments')

#POST ROUTE TO CREATE COMMENTS
@comments.route('/new_post', methods=['POST'] )
def new_comment():
    try:
        payload = request.get_json()
        print(payload)
        comment = models.Comment.create(**payload)
        comment_dict = model_to_dict(comment)
        del comment_dict['user_id']['password']
        return jsonify(data=comment_dict, status={'code': 201, 'message': 'comment successfully recorded'})
    except models.DoesNotExist:
        return jsonify(data={}, status={'code': 404, 'message': 'Error getting resources'})


#GET ROUTE TO DISPLAY COMMENTS ON LANDING PAGE
@comments.route('/get_all', methods=['GET'])
def get_all():
    try:
        get_query = models.Comment.select().order_by(models.Comment.id.desc())
        comments_to_dict = [model_to_dict(comments) for comments in get_query]
        for item in comments_to_dict:
            del item['user_id']['password']
        return jsonify(data=comments_to_dict, status={'code': 201, 'message': 'scores returned'})
    except models.DoesNotExist:
        return jsonify(data={}, status={'code': 404, 'message': 'Error getting resources'})

#GET ROUTE TO DISPLAY COMMENTS ON PROFILE PAGE
@comments.route('/get_comments/<player_id>', methods=['GET'])
def get_user_comments(player_id):
    try:
        user_comments_query = models.Comment.select().where(models.Comment.user_id == player_id)
        comments_to_dict = [model_to_dict(comments) for comments in user_comments_query]
        for item in comments_to_dict:
            del item['user_id']['password']
        return jsonify(data=comments_to_dict, status={'code': 201, 'message': 'scores returned'})
    except models.DoesNotExist:
        return jsonify(data={}, status={'code': 404, 'message': 'Error getting resources'})


#PUT ROUTE TO UPDATE COMMENTS

#DELETE ROUTE
@comments.route('/<comment_id>', methods=['Delete'])
def delete_one(comment_id):
    try:
        comment_to_delete = models.Comment.get_by_id(comment_id)
        comment_to_delete.delete_instance()
        return jsonify(data={}, status={'code': 200, 'message': 'Record successfully deleted'})
    except models.DoesNotExist:
        return jsonify(data={}, status={'code': 404,'message': 'Error getting resources'})