from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PORT'] = 9000
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'pass'
app.config['MYSQL_DB'] = 'DRS_PROJEKAT'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'


db = MySQL(app)

import blueprints

if __name__ == "__main__":
    app.register_blueprint(blueprints.user_blueprint, url_prefix='/user')
    app.register_blueprint(blueprints.card_blueprint, url_prefix='/card')
    app.register_blueprint(blueprints.transaction_blueprint, url_prefix='/transaction')
    app.run(host="0.0.0.0", port=15002, debug=True)
