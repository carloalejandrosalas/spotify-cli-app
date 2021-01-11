import requests

class HttpClient : 
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