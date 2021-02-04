import models

from flask import Blueprint, jsonify, request
from flask_login import current_user

from playhouse.shortcuts import model_to_dict

#set up blueprint to be used in decorators

#POST ROUTE TO REGISTER AMOUNT "WON" IN EACH GAME

