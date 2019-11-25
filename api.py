import requests
import itertools
from datetime import datetime
import constant
import timeanddate

def doLogin(email: str, password: str) -> str:
    loginEndpoint = "check_login/"
    loginPayload = { 'nome': '', 'id_sede': constant.BOX_ID, 'pass': password, 'mail': email, 'tipo': 'android', 'versione': '3.13.6'}
    r = requests.post(constant.BASE_URL + loginEndpoint,
                  data=loginPayload, headers=constant.HEADERS)
    session = r.json().get('parametri').get('sessione')
    if session is not None:
        return session.get('codice_sessione')
    else:
        return "Invalid credentials"

def getUsername(token: str) -> str:
    getUsernameEndpoint = "informazioni_utente/"
    getUsernamePayload = {'id_sede': constant.BOX_ID, 'codice_sessione': token}
    r = requests.post(constant.BASE_URL + getUsernameEndpoint,
                  data=getUsernamePayload, headers=constant.HEADERS)
    return r.json().get('parametri').get('cliente').get('nome')

def getClassId(token: str, date: datetime, time: datetime) -> str:
    getClassesEndpoint = "palinsesto_completo"
    getClassesPayload = {'id_sede': constant.BOX_ID,
                     'codice_sessione': token, 'giorno': timeanddate.stringFromDateTime(date, constant.INPUT_DATE_FORMAT)}
    r = requests.post(constant.BASE_URL + getClassesEndpoint,
                  data=getClassesPayload, headers=constant.HEADERS)
    daysList = r.json().get('parametri').get('lista_risultati')
    if daysList is not None:
        filteredDays = itertools.filterfalse(lambda x: datetime.strptime(
            x.get('nome_giorno'), constant.CLASSES_RESULT_DATE_FORMAT) != date, daysList)
        classes = list(filteredDays).pop().get('orari_palinsesto')
        filteredClasses = itertools.filterfalse(lambda x: datetime.strptime(
            x.get('orario_inizio'), constant.INPUT_TIME_FORMAT) != time, classes)
        return list(filteredClasses).pop().get('id_orario_palinsesto')

def doReservation(classId: str, token: str, date: datetime) -> str:
    reservationEndpoint = "prenotazione_new/"
    reservationPayload = {'id_orario_palinsesto': classId, 'id_sede': constant.BOX_ID,
                      'codice_sessione': token, 'data': timeanddate.stringFromDateTime(date, constant.INPUT_DATE_FORMAT)}
    r = requests.post(constant.BASE_URL + reservationEndpoint,
                  data=reservationPayload, headers=constant.HEADERS)
    return r.json().get('messaggio')