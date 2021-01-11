import settings
from services import init
from core.Spotify import Spotify

login = init.auth()

if not login :
    print('Error, the app cannot access to Spotify. Please check your internet connection')
else :
    app = Spotify()
    
