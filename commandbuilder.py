import platform

def buildCommand(classId: str, token: str, date: str, path: str, runTime: str, iteration: int) -> str:
  # if platform.system() == "Linux":
    if iteration == 0:
      return f'echo "python {path}reservo.py -classId {classId} -token {token} -date {date}" | at tomorrow {runTime}'
    else:
      return f'echo "sleep {iteration * 0.25} ; python {path}reservo.py -classId {classId} -token {token} -date {date}" | at {runTime} tomorrow'

