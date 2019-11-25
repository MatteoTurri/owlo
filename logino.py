import argparse
import api

parser = argparse.ArgumentParser(
    description='Logs in CrossFit Avanguardia system and returns a token if successful.')
parser.add_argument('-email', required=True)
parser.add_argument('-password', required=True)

args = parser.parse_args()

token = api.doLogin(args.email, args.password)
print(token)
