from flask import Blueprint
import databaseCRUD
import flask

user_blueprint = Blueprint('user_blueprint', __name__)


@user_blueprint.route('/getUserByEmail', methods=['GET', 'POST'])
def getUser():
    # TO DO: get user by email
    content = flask.request.json
    _email = content['email']
    _password = content['password']

    _user = databaseCRUD.getByEmail(_email)

    if _user is not None:
        if _password == _user['Lozinka']:
            return {'user': _user, 'message': 'Uspešno ulogovan!'}, 200
        else:
            return {'message': 'Pogrešna lozinka!'}, 400
    return {'message': 'Korisnik ne postoji!'}, 400


@user_blueprint.route('/insertUser', methods=['POST'])
def insertUser():
    # insertovanje korisnika u bazu
    content = flask.request.json
    ime = content['ime']
    prezime = content['prezime']
    adresa = content['adresa']
    grad = content['grad']
    drzava = content['drzava']
    brTel = content['brTelefona']
    email = content['email']
    lozinka = content['lozinka']
    brojKartice = 0
    novcanoStanje = 0
    verifikovan = 0
    valuta = "RSD"
    parametri = [ime, prezime, adresa, grad, drzava, brTel, email, lozinka, brojKartice, novcanoStanje, verifikovan,
                 valuta]

    _user = databaseCRUD.getByEmail(email)

    if _user is None:
        databaseCRUD.insert(parametri)
        return {'message': 'Korisnik uspesno registrovan!'}, 200
    return {'message': 'Korisnik vec postoji!'}, 400


@user_blueprint.route('/deleteUserByEmail', methods=['DELETE'])
def deleteUserByEmail():
    content = flask.request.json
    email = content['Email']
    databaseCRUD.deleteByEmail(email)

    return "Ok"


@user_blueprint.route('/updateUser', methods=['POST'])
def updateUser():
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

    databaseCRUD.update(parametri)

    return "Ok"
