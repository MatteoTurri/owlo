import json

def notContains(list, filter):
  for x in list:
    if filter(x):
      return False
  return True

def search(list, predicate):
  for x in list:
    if predicate(x):
      return x
  return None

def readData():
  try:
    with open('data.json') as json_file:
      return json.load(json_file)
  except IOError:
    data = {}
    data['users'] = []
    return data

def saveData(data):
  with open('data.json', 'w') as outfile:
    json.dump(data, outfile)

def readSchedule():
  with open('schedule.json') as json_file:
    return json.load(json_file)

