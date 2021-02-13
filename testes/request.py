import requests

url = 'http://127.0.0.1:6678/map'

res = requests.get(url)

print(res)