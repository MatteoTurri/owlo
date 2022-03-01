import locale
import argparse
import api
import timeanddate
import constant
import os
import utils
import asyncio
import os
from datetime import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import logging
from datetime import timedelta

parser = argparse.ArgumentParser(
    description='Schedules reservation requests.')
parser.add_argument('-scheduledDatetime', required=True, help='datetime when requests should be made, format YYYY-mm-dd_HH:MM')

args = parser.parse_args()

scheduledDatetime: str = args.scheduledDatetime

locale.setlocale(locale.LC_ALL, 'it_IT.UTF-8')

parsedScheduledDatetime = timeanddate.parseDateTime(scheduledDatetime, constant.INPUT_DATETIME_FORMAT)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', filename='log.log', filemode='a')
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
logger = logging.getLogger('reservo')

scheduler = AsyncIOScheduler({
    'apscheduler.executors.default': {
        'class': 'apscheduler.executors.pool:ThreadPoolExecutor',
        'max_workers': '25'
    }
})
scheduler.start()

schedule = utils.readSchedule()
days = schedule.get('schedule')

for d in days:
    data = utils.readData()
    tokens = []
    users = d.get('users')
    date = timeanddate.parseDateTime(d.get('day'), constant.INPUT_DATE_FORMAT)
    time = timeanddate.parseDateTime(d.get('time'), constant.INPUT_TIME_FORMAT)
    for u in users:
        tokens.append(utils.search(data.get('users'), lambda x: x.get('name') == u).get('token'))
    for t in tokens:
        print(api.getUsername(t))
    classId = api.getClassId(tokens[0], date, time)

    logger.info(f'Day: {date} - Tokens: {tokens}')

    for t in tokens:
        logger.info(f'Current token: {t}')
        scheduler.add_job(api.doReservation, 'date', run_date=parsedScheduledDatetime - timedelta(seconds=1), args=[classId, t, date, logger], misfire_grace_time=5)
        scheduler.add_job(api.doReservation, 'date', run_date=parsedScheduledDatetime, args=[classId, t, date, logger], misfire_grace_time=5)
        scheduler.add_job(api.doReservation, 'date', run_date=parsedScheduledDatetime + timedelta(seconds=1), args=[classId, t, date, logger], misfire_grace_time=5)
        scheduler.add_job(api.doReservation, 'date', run_date=parsedScheduledDatetime + timedelta(seconds=2), args=[classId, t, date, logger], misfire_grace_time=5)
        scheduler.add_job(api.doReservation, 'date', run_date=parsedScheduledDatetime + timedelta(seconds=3), args=[classId, t, date, logger], misfire_grace_time=5)
        scheduler.add_job(api.doReservation, 'date', run_date=parsedScheduledDatetime + timedelta(seconds=4), args=[classId, t, date, logger], misfire_grace_time=5)
        scheduler.add_job(api.doReservation, 'date', run_date=parsedScheduledDatetime + timedelta(seconds=8), args=[classId, t, date, logger], misfire_grace_time=5)
        scheduler.add_job(api.doReservation, 'date', run_date=parsedScheduledDatetime + timedelta(seconds=15), args=[classId, t, date, logger], misfire_grace_time=5)
        scheduler.add_job(api.doReservation, 'date', run_date=parsedScheduledDatetime + timedelta(seconds=30), args=[classId, t, date, logger], misfire_grace_time=5)
        scheduler.add_job(api.doReservation, 'date', run_date=parsedScheduledDatetime + timedelta(seconds=45), args=[classId, t, date, logger], misfire_grace_time=5)
        scheduler.add_job(api.doReservation, 'date', run_date=parsedScheduledDatetime + timedelta(minutes=1), args=[classId, t, date, logger], misfire_grace_time=5)
        scheduler.add_job(api.doReservation, 'date', run_date=parsedScheduledDatetime + timedelta(seconds=90), args=[classId, t, date, logger], misfire_grace_time=5)
        scheduler.add_job(api.doReservation, 'date', run_date=parsedScheduledDatetime + timedelta(minutes=2), args=[classId, t, date, logger], misfire_grace_time=5)
        scheduler.add_job(api.doReservation, 'date', run_date=parsedScheduledDatetime + timedelta(minutes=3), args=[classId, t, date, logger], misfire_grace_time=5)
        scheduler.add_job(api.doReservation, 'date', run_date=parsedScheduledDatetime + timedelta(minutes=4), args=[classId, t, date, logger], misfire_grace_time=5)
        scheduler.add_job(api.doReservation, 'date', run_date=parsedScheduledDatetime + timedelta(minutes=5), args=[classId, t, date, logger], misfire_grace_time=5)
        scheduler.add_job(api.doReservation, 'date', run_date=parsedScheduledDatetime + timedelta(minutes=6), args=[classId, t, date, logger], misfire_grace_time=5)
        scheduler.add_job(api.doReservation, 'date', run_date=parsedScheduledDatetime + timedelta(minutes=7), args=[classId, t, date, logger], misfire_grace_time=5)
        scheduler.add_job(api.doReservation, 'date', run_date=parsedScheduledDatetime + timedelta(minutes=8), args=[classId, t, date, logger], misfire_grace_time=5)
        scheduler.add_job(api.doReservation, 'date', run_date=parsedScheduledDatetime + timedelta(minutes=9), args=[classId, t, date, logger], misfire_grace_time=5)
        scheduler.add_job(api.doReservation, 'date', run_date=parsedScheduledDatetime + timedelta(minutes=10), args=[classId, t, date, logger], misfire_grace_time=5)
        scheduler.add_job(api.doReservation, 'date', run_date=parsedScheduledDatetime + timedelta(minutes=11), args=[classId, t, date, logger], misfire_grace_time=5)
        scheduler.add_job(api.doReservation, 'date', run_date=parsedScheduledDatetime + timedelta(minutes=12), args=[classId, t, date, logger], misfire_grace_time=5)
        scheduler.add_job(api.doReservation, 'date', run_date=parsedScheduledDatetime + timedelta(minutes=13), args=[classId, t, date, logger], misfire_grace_time=5)
        scheduler.add_job(api.doReservation, 'date', run_date=parsedScheduledDatetime + timedelta(minutes=14), args=[classId, t, date, logger], misfire_grace_time=5)
        scheduler.add_job(api.doReservation, 'date', run_date=parsedScheduledDatetime + timedelta(minutes=15), args=[classId, t, date, logger], misfire_grace_time=5)
        scheduler.add_job(api.doReservation, 'date', run_date=parsedScheduledDatetime + timedelta(minutes=20), args=[classId, t, date, logger], misfire_grace_time=5)
        scheduler.add_job(api.doReservation, 'date', run_date=parsedScheduledDatetime + timedelta(minutes=25), args=[classId, t, date, logger], misfire_grace_time=5)
        scheduler.add_job(api.doReservation, 'date', run_date=parsedScheduledDatetime + timedelta(minutes=30), args=[classId, t, date, logger], misfire_grace_time=5)
        scheduler.add_job(api.doReservation, 'date', run_date=parsedScheduledDatetime + timedelta(minutes=35), args=[classId, t, date, logger], misfire_grace_time=5)
        scheduler.add_job(api.doReservation, 'date', run_date=parsedScheduledDatetime + timedelta(minutes=40), args=[classId, t, date, logger], misfire_grace_time=5)
        scheduler.add_job(api.doReservation, 'date', run_date=parsedScheduledDatetime + timedelta(minutes=45), args=[classId, t, date, logger], misfire_grace_time=5)

print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

try:
    asyncio.get_event_loop().run_forever()
except (KeyboardInterrupt, SystemExit):
    pass
