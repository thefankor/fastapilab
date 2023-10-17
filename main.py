import requests

a = requests.get('http://127.0.0.1:8000/multi/RitaTheBestGIrl?jokes_number=5').json()

print(a)