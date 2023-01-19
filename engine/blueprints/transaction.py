from flask import Blueprint
import databaseCRUD
import flask
import threading
import MySQLdb

from multiprocessing import Queue
from time import sleep
from models.Transaction1 import Transaction1

queue = Queue()

transaction_blueprint = Blueprint('transaction_blueprint', __name__)


@transaction_blueprint.route('/getAllTransactionsForUser', methods=['GET'])
def getAllTransactionsForUser():
    content = flask.request.json
    _email = content['Email']
    _user = databaseCRUD.getByEmail(_email)
    _transactions = databaseCRUD.getAllTransactionsForUser(_user['BrojKartice'])

    return {'Transakcije': _transactions}, 200


@transaction_blueprint.route('/initTransaction1', methods=['POST'])
def initTransaction1():
    content = flask.request.json
    _sender = content['Posiljalac']
    _receiver = content['Primalac']
    _amount = content['Kolicina']
    _currency = content['Valuta']
    _rates = content['OdnosiZaKonverziju']
    _id = databaseCRUD.getLastTransactionId()

    parametri = [_sender, _receiver, _amount, "U OBRADI", _currency]
    databaseCRUD.insertTransaction1(parametri)

    _transakcija = Transaction1(_id, _sender, _receiver, _amount, _rates, _currency)

    thread = threading.Thread(target=transactionThread, args=(_transakcija,))
    thread.start()

    return "Ok"


###############
#### METODE ###
###############

def transactionThread(transakcija):
    print('New thread started.')

    sleep(5)

    queue.put(transakcija)


def transactionProcess(queue: Queue):
    while 1:
        print("[PROCESS] Waiting for a new transaction")
        transaction = queue.get()
        print(transaction.transactionId,transaction.receiver,transaction.sender)
        print(f"Transaction ID=[{transaction.transactionId}] started.")

        if isinstance(transaction, Transaction1):
            # Online - Online
            mydb = MySQLdb.connect(host="localhost",user="root",passwd="pass",db="DRS_PROJEKAT",port=9000)
            cursor = mydb.cursor()
            cursor.execute("SELECT * FROM Korisnik WHERE Korisnik.Email = %s",(transaction.sender,))
            _senderUser = cursor.fetchone()
            cursor.close()

            print("Usao 1")
            cursor = mydb.cursor()
            cursor.execute("SELECT * FROM Korisnik WHERE Korisnik.Email = %s", (transaction.receiver,))
            _receiverUser = cursor.fetchone()
            cursor.close()
            print(_receiverUser)

            _oduzeti = 0
            if _senderUser is not None and _receiverUser is not None:

                if str(_senderUser[11]) == str(transaction.currency):
                    # Nije se menjala valuta posiljaoca
                    _oduzeti = transaction.senderAmount
                else:
                    # Promenila se valuta posiljaoca, neophodna konverzija
                    _oduzeti = float(transaction.senderAmount) * transaction.conversionRates[_senderUser[11]]

                _novoStanjePosiljaoca = _senderUser[9] - _oduzeti

                if _novoStanjePosiljaoca >= 0:
                    # Promeni stanje korisniku koji je uplatio novac
                    cursor = mydb.cursor()
                    cursor.execute("UPDATE Korisnik SET NovcanoStanje = %s WHERE Email = %s ", (_novoStanjePosiljaoca,transaction.sender,))
                    cursor.close()

                    # Konvertovanje u valutu primaoca

                    _dodati = float(transaction.senderAmount) * transaction.conversionRates[_receiverUser[11]]

                    # Promeni stanje korisniku kojem se uplacuje novac

                    _novoStanjePrimaoca = _receiverUser[9] + _dodati
                    cursor = mydb.cursor()
                    cursor.execute("UPDATE Korisnik SET NovcanoStanje = %s WHERE Email = %s ",
                                   (_novoStanjePrimaoca, transaction.receiver,))

                    cursor.close()

                    # Transakcija uspesna

                    cursor = mydb.cursor()
                    cursor.execute("UPDATE Transakcija SET StatusTransakcije = %s WHERE IdTransakcije = %s;",
                                   ("OBRADJENO", transaction.transactionId,))
                    mydb.commit()
                    cursor.close()

                else:

                    cursor = mydb.cursor()
                    cursor.execute("UPDATE Transakcija SET StatusTransakcije = %s WHERE IdTransakcije = %s;",
                                   ("ODBIJENO", transaction.transactionId,))
                    mydb.commit()
                    cursor.close()

            else:
                cursor = mydb.cursor()
                cursor.execute("UPDATE Transakcija SET StatusTransakcije = %s WHERE IdTransakcije = %s;",
                               ("ODBIJENO", transaction.transactionId,))
                mydb.commit()
                cursor.close()
