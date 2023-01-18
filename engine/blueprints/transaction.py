from flask import Blueprint
import databaseCRUD
import flask

transaction_blueprint = Blueprint('transaction_blueprint', __name__)


@transaction_blueprint.route('/getAllTransactionsForUser', methods=['GET'])
def getAllTransactionsForUser():
    content = flask.request.json
    _email = content['Email']
    _user = databaseCRUD.getByEmail(_email)
    _transactions = databaseCRUD.getAllTransactionsForUser(_user['BrojKartice'])

    return {'Transakcije': _transactions}, 200


@transaction_blueprint.route('/insertTransaction', methods=['POST'])
def insertTransaction():
    content = flask.request.json
    _brojKartice = content['BrojKarticeKorisnika']
    _kolicina = content['KolicinaNovca']
    _status = content['StatusTransakcije']
    parametri = [_brojKartice, _kolicina, _status]
    databaseCRUD.insertTransaction(parametri)

    return "Ok"