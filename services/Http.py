from modules.HttpClient import HttpClient
from constants.credencials import values

http = HttpClient(values.get('API_URL'))
