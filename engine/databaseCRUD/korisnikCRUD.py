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


def insert(mysql: type(MySQL), args) -> dict:
    if len(args) > 12:
        return -5

    _ime = args[0]
    _prezime = args[1]
    _adresa = args[2]
    _grad = args[3]
    _drzava = args[4]
    _brTelefona = args[5]
    _email = args[6]
    _lozinka = args[7]
    _brKartice = args[8]
    _novcanoStanje = args[9]
    _verifikovan = args[10]
    _valuta = args[11]

    _query = """INSERT INTO Korisnik (Ime, Prezime, Adresa, Grad, Drzava, BrojTelefona, Email, Lozinka, BrojKartice, 
    NovcanoStanje, Verifikovan, Valuta) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s); """

    try:
        with mysql.connection.cursor() as cursor:
            data = (_ime, _prezime, _adresa, _grad, _drzava, _brTelefona, _email, _lozinka, _brKartice, _novcanoStanje,
                    _verifikovan, _valuta)
            cursor.execute(_query, data)
            mysql.connection.commit()
    except NameError:
        print(NameError.name)

        return {}.get('missing_key', None)