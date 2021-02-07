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


#GET ROUTE TO DISPLAY COMMENTS

#PUT ROUTE TO UPDATE COMMENTS

#DELETE ROUTE