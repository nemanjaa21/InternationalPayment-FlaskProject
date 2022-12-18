from flask import Flask, Blueprint, render_template, request, json, session

account_blueprint = Blueprint('account_blueprint', __name__)