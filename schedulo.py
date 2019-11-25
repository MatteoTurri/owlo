import locale
import argparse
import api
import timeanddate
import commandbuilder
import constant
import os

parser = argparse.ArgumentParser(
    description='Schedules a reservation request for a CrossFit Avanguardia class.')
parser.add_argument('-date', required=True,
                    help='date of the selected class, format YYYY-MM-DD')
parser.add_argument('-time', required=True, help='time of the selected class, format HH:MM')
parser.add_argument('-token', nargs='+', help='authentication token(s)')
parser.add_argument('-path', required=True, help='path of the folder where reservo.py script is')
parser.add_argument('-scheduledTime', required=True, help='time when the reservation request should be made, format HHMM')
parser.add_argument('-nReq', required=True, type=int, help='number of per-user request that should be made')

args = parser.parse_args()
inputDate: str = args.date
inputTime: str = args.time
tokens = args.token
path: str = args.path
scheduledTime: str = args.scheduledTime
nReq: int = args.nReq

locale.setlocale(locale.LC_ALL, 'it_IT.UTF-8')

parsedDate = timeanddate.parseDateTime(inputDate, constant.INPUT_DATE_FORMAT)
parsedTime = timeanddate.parseDateTime(inputTime, constant.INPUT_TIME_FORMAT)
parsedAtTime = timeanddate.parseDateTime(scheduledTime, constant.INPUT_TIME_FORMAT_AT)
validatedDate = timeanddate.stringFromDateTime(parsedDate, constant.INPUT_DATE_FORMAT)
validatedScheduledTime = timeanddate.stringFromDateTime(parsedAtTime, constant.INPUT_TIME_FORMAT_AT)

for t in tokens:
    print(api.getUsername(t))

classId = api.getClassId(tokens[0], parsedDate, parsedTime)

for t in tokens:
    for n in range(nReq):
        command = commandbuilder.buildCommand(classId, t, validatedDate, path, validatedScheduledTime, n)
        print(command)
        os.system(command)
