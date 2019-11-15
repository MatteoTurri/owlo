import requests
import itertools
from datetime import datetime
import locale
import argparse

parser = argparse.ArgumentParser(
    description='Makes a reservation for a CrossFit Avanguardia class on the selected date and time.')
parser.add_argument('-date', required=True,
                    help='selected date, format YYYY-MM-DD')
parser.add_argument('-time', required=True, help='selected time, format HH:MM')
parser.add_argument('-token', required=True, help='authentication token')

args = parser.parse_args()
inputDate = args.date
inputTime = args.time
token = args.token

locale.setlocale(locale.LC_ALL, 'it_IT.UTF-8')

baseUrl = "https://cfavanguardia.shaggyowl.com/funzioniapp/v341/"
idSede = 105
inputTimeFormat = '%H:%M'
inputDateFormat = '%Y-%m-%d'
headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
           'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 6.0; Android SDK built for x86_64 Build/MASTER)'}

parsedInputDate = datetime.strptime(inputDate, inputDateFormat)
processedInputDate = datetime.strftime(parsedInputDate, inputDateFormat)
parsedInputTime = datetime.strptime(inputTime, inputTimeFormat)

resultsDateFormat = '%A %d/%m/%Y'
getClassesEndpoint = "palinsesto_completo"
getClassesPayload = {'id_sede': idSede,
                     'codice_sessione': token, 'giorno': processedInputDate}
r = requests.post(baseUrl+getClassesEndpoint,
                  data=getClassesPayload, headers=headers)
daysList = r.json().get('parametri').get('lista_risultati')
filteredDays = itertools.filterfalse(lambda x: datetime.strptime(
    x.get('nome_giorno'), resultsDateFormat) != parsedInputDate, daysList)
classes = list(filteredDays).pop().get('orari_palinsesto')
filteredClasses = itertools.filterfalse(lambda x: datetime.strptime(
    x.get('orario_inizio'), inputTimeFormat) != parsedInputTime, classes)
classId = list(filteredClasses).pop().get('id_orario_palinsesto')

print(classId)

reservationEndpoint = "prenotazione_new/"
reservationPayload = {'id_orario_palinsesto': classId, 'id_sede': idSede,
                      'codice_sessione': token, 'data': processedInputDate}
r = requests.post(baseUrl+reservationEndpoint,
                  data=reservationPayload, headers=headers)
print(r.text)
