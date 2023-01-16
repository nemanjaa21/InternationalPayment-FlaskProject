from flask import Flask, Blueprint, render_template, request, json, redirect, url_for, session, flash

import requests

account_blueprint = Blueprint('account_blueprint', __name__)


@account_blueprint.route('/account', methods=['GET'])
def account():
    if 'user' not in session:
        return redirect(url_for('user_blueprint.login'))
    return render_template('nalog.html')


@account_blueprint.route('/edit', methods=['GET', 'POST'])
def edit():
    if 'user' not in session:
        return redirect(url_for('user_blueprint.login'))
    if request.method == 'GET':
        return render_template('izmenaProfila.html')
    elif request.method == 'POST':
        _ime = request.form['ime']
        _prezime = request.form['prezime']
        _adresa = request.form['adresa']
        _grad = request.form['grad']
        _drzava = request.form['drzava']
        _brTelefona = request.form['brojTelefona']
        _email = request.form['email']
        _lozinka = request.form['lozinka']
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        body = json.dumps({'ime': _ime, 'prezime': _prezime, 'adresa': _adresa, 'grad': _grad,
                           'drzava': _drzava, "brTelefona": _brTelefona, 'email': _email,
                           'oldEmail': session['user']['Email'], 'lozinka': _lozinka})
        req = requests.post("http://127.0.0.1:15002/user/updateUser", data=body, headers=headers)
        response = (req.json())
        _code = req.status_code

        if _code == 200:
            body = json.dumps({'email': _email, 'password': _lozinka})
            req = requests.post("http://127.0.0.1:15002/user/getUserByEmail", data=body, headers=headers)
            response = (req.json())
            _code = req.status_code

            if _code == 200:
                _user = response['user']
                session.permanent = False
                session['user'] = _user
                return redirect(url_for('account_blueprint.account'))
            else:
                return render_template("index.html")

        return redirect(url_for('account_blueprint.account'))


@account_blueprint.route('/verify', methods=['POST'])
def verify():
    if 'user' not in session:
        return redirect(url_for('user_blueprint.login'))

    _brKartice = request.form['brKartice']
    _ime = request.form['ime']
    _datum = request.form['datum']
    _kod = request.form['kod']
    _email = session['user']['Email']

    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    body = json.dumps({'brKartice': _brKartice, 'ime': _ime, 'datum': _datum, 'sigurnosniKod': _kod, 'email': _email})
    req = requests.post("http://127.0.0.1:15002/user/updateUserCardNumber", data=body, headers=headers)
    response = (req.json())
    _code = req.status_code
    _message = response['message']

    if _code == 400:
        return render_template("nalog.html", message=_message)
    elif _code == 200:
        session['user']['Verifikovan'] = 1
        return render_template("nalog.html")


@account_blueprint.route('addMoney', methods=['POST'])
def addMoney():
    if 'user' not in session:
        return render_template("user_blueprint.login");
    _email = session['user']['Email']
    _kolicina = request.form['unosNovca']

    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    body = json.dumps({'Email': _email, 'NovcanoStanje': _kolicina})
    req = requests.post("http://127.0.0.1:15002/user/transferMoney", data=body, headers=headers)
    response = (req.json())
    _code = req.status_code
    _message = response['message']

    if _code == 400:
        session['message'] = _message
        return render_template("nalog.html", message=_message)
    elif _code == 200:
        _stanje = response['stanje']
        session['user']['NovcanoStanje'] = _stanje
        return render_template("nalog.html")


@account_blueprint.route('changeCurrency', methods=['POST', 'GET'])
def changeCurrency():
    if 'user' not in session:
        return render_template("user_blueprint.login");

    _valutaTrenutna = session['user']['Valuta'];
    _novcanoStanjeTrenutno = session['user']['NovcanoStanje']
    _email = session['user']['Email']

    URL = f"https://v6.exchangerate-api.com/v6/84da0ca6eca0cde00ef3f0ac/latest/{_valutaTrenutna}"
    r = requests.get(url=URL)
    data = r.json();

    _valutaUKojuPrebacujem = request.form['valuta2'];
    _rate = data['conversion_rates'][f'{_valutaUKojuPrebacujem}'];
    _convertedValue = _novcanoStanjeTrenutno * _rate;
    _convertedValue = round(_convertedValue, 2);

    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    body = json.dumps(
        {'ConvertedValue': _convertedValue, 'ValutaUKojuPrebacujem': _valutaUKojuPrebacujem, 'Email': _email})
    req = requests.post("http://127.0.0.1:15002/user/changeCurrency", data=body, headers=headers)
    response = (req.json())
    _code = req.status_code
    _message = response['message']
    session['user']['Valuta'] = _valutaUKojuPrebacujem
    session['user']['NovcanoStanje'] = _convertedValue

    return render_template("nalog.html");
