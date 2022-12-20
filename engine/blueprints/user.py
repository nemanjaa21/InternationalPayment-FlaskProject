from flask import Blueprint
import databaseCRUD
import flask

from main import mysql

user_blueprint = Blueprint('user_blueprint', __name__)


@user_blueprint.route('/getUserByEmail', methods=['GET'])
def getUser():
    # TO DO: get user by email
    content = flask.request.json
    _email = content['Email']

    _user = databaseCRUD.getByEmail(mysql, _email)

    return {'User': _user}, 200

