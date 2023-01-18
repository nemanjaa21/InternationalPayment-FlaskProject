from app import db


def getAllTransactionsForUser(BrojKarticeKorisnika: str) -> dict:
    _query = "SELECT * FROM Transakcija WHERE BrojKarticeKorisnika = %(BrojKarticeKorisnika)s"

    try:
        with db.connection.cursor() as cursor:
            cursor.execute(_query, {'BrojKarticeKorisnika': BrojKarticeKorisnika})
            _transaction = cursor.fetchall()

            return _transaction
    except NameError:
        print(NameError.name)

        return {}.get('missing_key', None)


def insertTransaction(args) -> dict:
    if len(args) > 3:
        return -5

    _brKartice = args[0]
    _kolicinaNovca = args[1]
    _statusTransakcije = args[2]

    _query = """INSERT INTO Transakcija (BrojKarticeKorisnika, KolicinaNovca, StatusTransakcije) 
    VALUES (%s, %s, %s); """

    try:
        with db.connection.cursor() as cursor:
            data = (_brKartice, _kolicinaNovca, _statusTransakcije)
            cursor.execute(_query, data)
            db.connection.commit()
    except NameError:
        print(NameError.name)

        return {}.get('missing_key', None)