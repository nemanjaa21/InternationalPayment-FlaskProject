from flask import Blueprint
import databaseCRUD
import flask
import threading

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


@transaction_blueprint.route('/insertTransaction', methods=['POST'])
def insertTransaction():
    content = flask.request.json
    _brojKartice = content['BrojKarticeKorisnika']
    _kolicina = content['KolicinaNovca']
    _status = content['StatusTransakcije']
    parametri = [_brojKartice, _kolicina, _status]
    databaseCRUD.insertTransaction(parametri)

    return "Ok"


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
    databaseCRUD.insertTransaction(parametri)

    _transakcija = Transaction1(_id, _sender, _receiver, _amount, _rates, _currency)

    thread = threading.Thread(target=transactionThread, args=(_transakcija,))
    thread.start()

    return "Ok"


###############
#### METODE ###
###############

def transactionThread(transakcija):
    print('New thread started.')

    sleep(30)

    queue.put(transakcija)

def transactionProcess(queue: Queue):
    while 1:
        print("[PROCESS] Waiting for a new transaction")
        transaction = queue.get()
        print(f"Transaction ID=[{transaction.transactionId}] started.")

        if isinstance(transaction, Transaction1):
            # Online - Online
            _senderUser = databaseCRUD.getByEmail(transaction.sender)
            _receiverUser = databaseCRUD.getByEmail(transaction.receiver)

            _oduzeti = 0
            if _senderUser is not None:

                if str(_senderUser['Valuta']) == str(transaction.currency):
                    # Nije se menjala valuta posiljaoca
                    _oduzeti = transaction.senderAmount
                else:
                    # Promenila se valuta posiljaoca, neophodna konverzija
                    _oduzeti = float(transaction.senderAmount) * transaction.currency[str(_senderUser['Valuta'])]

                _novoStanjePosiljaoca = _senderUser['NovcanoStanje'] - _oduzeti

                if _novoStanjePosiljaoca >= 0:
                    # Promeni stanje korisniku koji je uplatio novac

                    databaseCRUD.updateUserBalance([transaction.sender, _novoStanjePosiljaoca])

                    # Konvertovanje u valutu primaoca

                    _dodati = float(transaction.senderAmount) * transaction.currency(str(_receiverUser['Valuta']))

                    # Promeni stanje korisniku kojem se uplacuje novac

                    _novoStanjePrimaoca = _receiverUser['NovcanoStanje'] + _dodati

                    databaseCRUD.updateUserBalance([transaction.receiver, _novoStanjePrimaoca])

                    # Transakcija uspesna
                    parametri = [transaction.transactionId, "OBRADJENO"]
                    databaseCRUD.updateTransaction1(parametri)
                else:
                    parametri = [transaction.transactionId, "ODBIJENO"]
                    databaseCRUD.updateTransaction1(parametri)
            else:
                parametri = [transaction.transactionId, "ODBIJENO"]
                databaseCRUD.updateTransaction1(parametri)
