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


def updateTransaction1(args) -> dict:
    if len(args) > 2:
        return {}.get('missing_key', None)

    _id = args[0]
    _status = args[1]

    _query = """UPDATE Transakcija SET StatusTransakcije = %s WHERE IdTransakcije = %s;"""

    try:
        with db.connection.cursor() as cursor:
            data = (_id, _status)
            cursor.execute(_query, data)
            db.connection.commit()
    except NameError:
        print(NameError.name)

        return {}.get('missing_key', None)


def getLastTransactionId() -> int:
    _query = "SELECT IdTransakcije FROM Transakcija ORDER BY IdTransakcije DESC"
    try:
        with db.connection.cursor() as cursor:
            cursor.execute(_query)
            _transactionId = cursor.fetchone()

            if _transactionId:
                return _transactionId['IdTransakcije'] + 1
            else:
                return 1
    except NameError:
        print(NameError.name)


def insertTransaction1(args):
    if len(args) > 5:
        return -5

    _posiljalac = args[0]
    _primalac = args[1]
    _kolicinaNovca = args[2]
    _status = args[3]
    _valuta = args[4]

    _query = """INSERT INTO Transakcija (Posiljalac, Primalac, KolicinaNovca, StatusTransakcije, Valuta) 
    VALUES (%s, %s, %s, %s, %s); """

    try:
        with db.connection.cursor() as cursor:
            data = (_posiljalac, _primalac, _kolicinaNovca, _status, _valuta)
            cursor.execute(_query, data)
            db.connection.commit()
    except NameError:
        print(NameError.name)
