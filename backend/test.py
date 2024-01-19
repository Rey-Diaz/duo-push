import duo_app
from pprint import pprint

def fetch_users():
    users = duo_app.duo_authenticator.fetch_users()
    pprint(users)
    print('Total users: {}'.format(len(users)))

def send_push(username):
    users = duo_app.duo_authenticator.fetch_users()
    user = [user for user in users if user['username'] == username][0]
    device = None
    for d in user['devices']:
        if d['type'] == 'phone' and 'push' in d['capabilities']:
            device = d
            print('Found device:')
            pprint(device)
            break
    result = duo_app.duo_authenticator.authenticate_user(username, auth_type='push', device=device['id'])
    print(result)

def send_sms(username):
    users = duo_app.duo_authenticator.fetch_users()
    user = [user for user in users if user['username'] == username][0]
    device = None
    for d in user['devices']:
        if d['type'] == 'phone' and 'sms' in d['capabilities']:
            device = d
            print('Found device:')
            pprint(device)
            break
    print(duo_app.duo_authenticator.authenticate_user(username, auth_type='sms', device=device['id']))
    code = input("Please enter the sms code: ")
    print('Got code: {}'.format(code))
    result = duo_app.duo_authenticator.authenticate_user(username, auth_type='passcode', passcode=code)
    print(result)

def send_passcode(username):
    code = input("Please enter the duo app code or hardware token: ")
    print('Got code: {}'.format(code))
    result = duo_app.duo_authenticator.authenticate_user(username, auth_type='passcode', passcode=code)
    print(result)

fetch_users()
#send_push('abc1234')
#send_sms('yh')
#send_passcode('yh')
