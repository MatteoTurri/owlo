import locale
import argparse
import api
import timeanddate
import constant

parser = argparse.ArgumentParser(
    description='Makes a reservation for a CrossFit Avanguardia class.')
parser.add_argument('-classId', required=True, help='identifier of the class')
parser.add_argument('-date', required=True,
                    help='selected date, format YYYY-MM-DD')
parser.add_argument('-token', nargs='+', help='authentication token')

args = parser.parse_args()
classId: str = args.classId
date: str = args.date
token: str = args.token

locale.setlocale(locale.LC_ALL, 'it_IT.UTF-8')

parsedDate = timeanddate.parseDateTime(date, constant.INPUT_DATE_FORMAT)

result = api.doReservation(classId, token, parsedDate)
print(result)
