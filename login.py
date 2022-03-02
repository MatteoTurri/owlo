import argparse
import api
import utils

parser = argparse.ArgumentParser(
    description='Logs in the target system and returns a token if successful.')
parser.add_argument('-email', required=True)
parser.add_argument('-password', required=True)
parser.add_argument('-alias', required=True)

args = parser.parse_args()
email = args.email
password = args.password
name = args.alias

data = utils.readData()

if utils.notContains(data.get('users'), lambda x: x.get('email') == email):
    token = api.doLogin(email, password)
    if token != 'Invalid credentials':
        data.get('users').append({'name': name, 'email': email, 'token': token})
        utils.saveData(data)
    print(token)
else:
    token = utils.search(data.get('users'), lambda x: x.get('email') == email).get('token')
    print(token)


