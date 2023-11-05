import socket
import requests
import pprint
import json

hostname = input('Masukkan Domain Target: ')
ip_address = socket.gethostbyname(hostname)

response = requests.get(f'https://geolocation-db.com/jsonp/{ip_address}')

geolocation = response.content.decode()
geolocation = geolocation.split('(')[1].strip(')')
geolocation = json.loads(geolocation)

for key, value in geolocation.items():
    pprint.pprint(f'{key} : {value}')
