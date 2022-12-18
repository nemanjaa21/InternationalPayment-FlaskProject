from flask import Flask, Blueprint, render_template, request, json, session

user_blueprint = Blueprint('user_blueprint', __name__)


@user_blueprint.route('/')
def index():
    # TO DO: index logic
    return render_template('index.html')


@user_blueprint.route('/register', methods=['POST', 'GET'])
def register():
    # TO DO: register logic
    return render_template('index.html')


@user_blueprint.route('/login', methods=['POST', 'GET'])
def login():
    # TO DO: login
    return render_template('login.html')
