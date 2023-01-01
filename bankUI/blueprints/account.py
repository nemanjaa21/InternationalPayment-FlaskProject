from flask import Flask, Blueprint, render_template, request, json, redirect, url_for, session

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
