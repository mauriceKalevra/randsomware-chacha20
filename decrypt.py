import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
from cryptography.hazmat.backends import default_backend

def decrypt_file_chacha20(key, input_file, output_file):
    # Überprüfen der Schlüssellänge und Anpassen, falls erforderlich
    if len(key) != 32:
        key = key[:32]  # Kürzen des Schlüssels auf 32 Bytes

    # Lesen des Inhalts der Eingabedatei
    with open(input_file, 'rb') as file:
        encrypted_data = file.read()

    # Extrahieren von Nonce, Ciphertext und Authentifizierungstag aus der verschlüsselten Datei
    nonce = encrypted_data[:12]
    ciphertext = encrypted_data[12:-16]
    tag = encrypted_data[-16:]

    # Erstellen einer ChaCha20Poly1305-Entschlüsselungsinstanz mit dem Schlüssel
    cipher = ChaCha20Poly1305(key)

    # Entschlüsseln der Daten
    decrypted_data = cipher.decrypt(nonce, ciphertext, None)

    # Schreiben der entschlüsselten Daten in die Ausgabedatei
    with open(output_file, 'wb') as file:
        file.write(decrypted_data)


key = b'adn\xf1\xa4 \xc4\xf8\xbb\xc7\xb2e\xc4\x00\xd3\xb1\x08\xb9\x0c\x15-+\x07\x9d~\xd8\x8f\xedn_5\x18'

input_file = 'verschluesselte_datei.bin'
output_file = 'entschluesselte_datei.txt'

decrypt_file_chacha20(key, input_file, output_file)

