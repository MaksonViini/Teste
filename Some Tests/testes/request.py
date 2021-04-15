import requests

url = 'http://127.0.0.1:5985/map'

res = requests.get(url)

print(res)
