from datetime import datetime
import constant

def parseDateTime(dateTime: str, timeformat: str) -> datetime:
  return datetime.strptime(dateTime, timeformat)

def stringFromDateTime(dateTime: datetime, timeformat: str) -> str:
  return dateTime.strftime(timeformat)
