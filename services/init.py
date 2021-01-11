import requests
from constants.credencials import values
from services.Http import http

client_id = values.get('CLIENT_ID')
client_secret = values.get('CLIENT_SECRET')

def auth() :
    endpoint = values.get('AUTH_URL')
    
    payload = { 'grant_type' : 'client_credentials' }
    
    auth = requests.auth.HTTPBasicAuth(client_id, client_secret)
    
    req = requests.post(endpoint, data=payload, auth=auth)

    if req.status_code == 400 or req.status_code == 500:
        print('******** BAD CONNECTION ********')
        return False

    response = req.json()

    access_token = response['access_token']
    
    http.headers = { 'authorization': 'Bearer '+ access_token }

    print('******** Connection successful ********')
    return True