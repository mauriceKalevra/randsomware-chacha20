import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
from cryptography.hazmat.backends import default_backend
import secrets

def encrypt_file_chacha20(key, input_file, output_file):
    # Lesen des Inhalts der Eingabedatei
    with open(input_file, 'rb') as file:
        plaintext = file.read()

    # Generieren eines zufälligen Nonces
    nonce = os.urandom(12)

    # Erstellen einer ChaCha20Poly1305-Verschlüsselungsinstanz mit dem Schlüssel und Nonce
    cipher = ChaCha20Poly1305(key)

    # Verschlüsseln der Daten
    ciphertext = cipher.encrypt(nonce, plaintext, None)

    # Schreiben des verschlüsselten Texts, Nonces und Authentifizierungstag in die Ausgabedatei
    with open(output_file, 'wb') as file:
        file.write(ciphertext )


def generate_random_key():
    key = secrets.token_bytes(32)
    print(key)
    return key

key = generate_random_key()

input_file = 'klartext.txt'
output_file = 'verschluesselte_datei.bin'

encrypt_file_chacha20(key, input_file, output_file)

