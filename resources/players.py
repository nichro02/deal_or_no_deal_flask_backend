import models

from flask import Blueprint, jsonify, request
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, current_user

from playhouse.shortcuts import model_to_dict

#set up blueprint to be used in decorators

#POST ROUTE TO REGISTER PLAYERS

#POST ROUTE TO LOGIN PLAYERS

#GET, POST ROUTE TO LOGOUT PLAYERS

#DELETE PLAYER