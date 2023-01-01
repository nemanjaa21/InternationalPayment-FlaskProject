from app import db


def getByNumber(BrojKartice: str) -> dict:
    _query = "SELECT * FROM Kartica WHERE BrojKartice = %(BrojKartice)s"

    try:
        with db.connection.cursor() as cursor:
            cursor.execute(_query, {'BrojKartice': BrojKartice})
            _card = cursor.fetchone()

            return _card
    except NameError:
        print(NameError.name)

        return {}.get('missing_key', None)


def insertC(args) -> dict:
    if len(args) > 5:
        return -6

    _brojKartice = args[0]
    _imeKorisnika = args[1]
    _datumIsteka = args[2]
    _novcanoStanje = args[3]
    _sigurnosniKod = args[4]

    _query = """INSERT INTO Kartica (BrojKartice, ImeKorisnika, DatumIsteka, NovcanoStanje, SigurnosniKod)
     VALUES (%s, %s, %s, %s, %s); """

    try:
        with db.connection.cursor() as cursor:
            data = (_brojKartice, _imeKorisnika, _datumIsteka, _novcanoStanje, _sigurnosniKod)
            cursor.execute(_query, data)
            db.connection.commit()
    except NameError:
        print(NameError.name)

        return {}.get('missing_key', None)


def deleteByNumber(BrojKartice) -> dict:
    _query = "DELETE FROM Kartica WHERE BrojKartice = %(BrojKartice)s"

    try:
        with db.connection.cursor() as cursor:
            cursor.execute(_query, {'BrojKartice': BrojKartice})
            db.connection.commit()

    except NameError:
        print(NameError.name)

        return {}.get('missing_key', None)


def updateC(args) -> dict:
    if len(args) > 5:
        return -6

    _brojKartice = args[0]
    _imeKorisnika = args[1]
    _datumIsteka = args[2]
    _novcanoStanje = args[3]
    _sigurnosniKod = args[4]

    _query = """UPDATE Kartica SET BrojKartice = %s, ImeKorisnika = %s, DatumIsteka = %s, NovcanoStanje = %s,
     SigurnosniKod = %s WHERE BrojKartice = %s """

    try:
        with db.connection.cursor() as cursor:
            data = (_brojKartice, _imeKorisnika, _datumIsteka, _novcanoStanje, _sigurnosniKod,_brojKartice)
            cursor.execute(_query, data)
            db.connection.commit()
    except NameError:
        print(NameError.name)

        return {}.get('missing_key', None)
