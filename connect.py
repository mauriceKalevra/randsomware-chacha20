import requests

# Server-Informationen
server_url = 'http://172.17.0.2:1337'
#api_key = 'your_api_key'

# Daten, die an den Server übergeben werden sollen
data = {'name': 'Max Mustermann', 'age': 30}

# Header mit API-Schlüssel
#headers = {'Authorization': f'Bearer {api_key}'}

# HTTP-POST-Anfrage an den Server senden
response = requests.post(server_url,json=data)

# Server-Antwort ausgeben
print(response.json())

