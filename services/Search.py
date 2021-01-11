from services.Http import http 

def general(query):

    params = {
        'q' : query,
        'type': 'artist,playlist,track',
        'limit': 10
    }
        
    req = http.get('/search', params)
    
    return req.json()

def songs(query):
    params: {
        'q' : query,
        'type': 'track',
        'limit': 10
    }
