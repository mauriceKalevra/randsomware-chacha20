import socket
import os
# Host-IP-Adresse und Port
host = '172.17.0.3'
port = 1234

# Socket erstellen und an die IP-Adresse und den Port binden
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))

# Auf eingehende Verbindungen warten
server_socket.listen(1)
print('Server läuft und wartet auf Verbindungen...')

# Verbindung akzeptieren
client_socket, client_address = server_socket.accept()
print('Verbunden mit:', client_address)

# Datei empfangen und speichern
os.mkdir("victim1")
os.chdir("victim1")
with open('empfangene_datei.txt', 'wb') as file:
    data = client_socket.recv(1024)
    while data:
        file.write(data)
        data = client_socket.recv(1024)

print('Datei erfolgreich empfangen und gespeichert.')

# Verbindung schließen
client_socket.close()
server_socket.close()

