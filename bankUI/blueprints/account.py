from flask import Flask, Blueprint, render_template, request, json, redirect, url_for, session

account_blueprint = Blueprint('account_blueprint', __name__)


@account_blueprint.route('/account', methods=['GET'])
def account():
    if 'user' not in session:
        return redirect(url_for('user_blueprint.login'))
    return render_template('nalog.html')


@account_blueprint.route('/edit', methods=['GET'])
def edit():
    if 'user' not in session:
        return redirect(url_for('user_blueprint.login'))
    return render_template('izmenaProfila.html')
