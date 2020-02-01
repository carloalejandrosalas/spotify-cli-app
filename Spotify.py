from getpass import getpass
import requests
import base64

class Spotify :
    def __init__(self) :
        self.http = Http('https://api.spotify.com/v1')
        self.client_id = 'f6388e1a9898429f98ba332f1a058508'
        self.client_secret = 'db5078ba818642b0a7615858896a4995'
        self.access_token = ''

        self.auth()

    def search(self, query):
        params = {
            'q' : query,
            'type': 'artist,playlist,track'
        }
            
        req = self.http.get('/search', params)
        
        print(req.json())

    def auth(self) :
        endpoint = 'https://accounts.spotify.com/api/token'
        
        payload = { 'grant_type' : 'client_credentials' }
        
        credencials= requests.auth.HTTPBasicAuth(self.client_id, self.client_secret)
        
        req = requests.post(endpoint, data=payload, auth=credencials)

        if req.status_code == 400 or req.status_code == 500:
            return print('******** BAD CONNECTION ********')
            
        response = req.json()

        self.access_token = response['access_token']
        
        self.http.headers = { 'authorization': 'Bearer '+ self.access_token }

        print('******** Connection successful ********')

        self.ask()
    
    def ask(self):
        option = input("""
        1 - Search
        2 - Exit
        """) 

        if option == '1':
            query = input('Artist/Song/Playlist: ')
            self.search(query)

        

class Http : 
    """ Class to make HTTP requests  """
    def __init__(self, base_url, headers = {}) : 
        self.base_url = base_url
        self.headers = headers
    
    def get(self, endpoint, params = {} ,headers = {}) :
        
        headers.update(self.headers)

        req = requests.get(self.base_url + endpoint, params=params ,headers=headers)
        return req

    def post(self, endpoint, payload, headers = {}) : 
        
        headers.update(self.headers)
        
        req = requests.post(self.base_url + endpoint, data=payload, headers= headers)
        return req


# username = input('username/email: ')
# password = getpass()


app = Spotify()

# req = app.search('Rihanna')


# print(req)