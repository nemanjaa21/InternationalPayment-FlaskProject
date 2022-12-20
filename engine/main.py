from flask import Flask
from flask_mysqldb import MySQL
import blueprints

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PORT'] = 9000
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'pass'
app.config['MYSQL_DB'] = 'DRS_PROJEKAT'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'


mysql = MySQL(app)

if __name__ == "__main__":
    app.register_blueprint(blueprints.user_blueprint, url_prefix='/user')
    app.run(host="0.0.0.0", port=15002, debug=True)
