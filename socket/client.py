import socket

# Host-IP-Adresse und Port
host = '172.17.0.3'
port = 1234

# Socket erstellen und Verbindung zum Host herstellen
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

# Datei öffnen und Inhalt in Pakete aufteilen
with open('daten.txt', 'rb') as file:
    data = file.read(1024)
    while data:
        client_socket.send(data)
        data = file.read(1024)

print('Datei erfolgreich gesendet.')

# Verbindung schließen
client_socket.close()

