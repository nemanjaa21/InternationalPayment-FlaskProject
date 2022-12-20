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


@user_blueprint.route('/insertUser', methods=['POST'])
def insertUser():
    # insertovanje korisnika u bazu
    content = flask.request.json
    ime = content['Ime']
    prezime = content['Prezime']
    adresa = content['Adresa']
    grad = content['Grad']
    drzava = content['Drzava']
    brTel = content['BrojTelefona']
    email = content['Email']
    lozinka = content['Lozinka']
    brojKartice = content['BrojKartice']
    novcanoStanje = content['NovcanoStanje']
    verifikovan = content['Verifikovan']
    valuta = content['Valuta']
    parametri = [ime, prezime, adresa, grad, drzava, brTel, email, lozinka, brojKartice, novcanoStanje, verifikovan,
                 valuta]

    _user = databaseCRUD.insert(mysql, parametri)

    return {'User': _user}, 200
