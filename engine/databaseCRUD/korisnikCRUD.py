from flask_mysqldb import MySQL


def getByEmail(mysql: type(MySQL), email: str) -> dict:
    _query = "SELECT * FROM Korisnik WHERE Korisnik.Email = %(email)s"

    try:
        with mysql.connection.cursor() as cursor:
            cursor.execute(_query, {'email': email})
            _user = cursor.fetchone()

            return _user
    except NameError:
        print(NameError.name)

        return {}.get('missing_key', None)
