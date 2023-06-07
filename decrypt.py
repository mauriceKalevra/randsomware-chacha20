def decrypt_file_chacha20(key, input_file, output_file):
    # Lesen des Inhalts der Eingabedatei
    with open(input_file, 'rb') as file:
        encrypted_data = file.read()

    # Extrahieren von Nonce und verschlüsselten Daten aus der Datei
    nonce = encrypted_data[:16]
    ciphertext = encrypted_data[16:]

    # Erstellen einer ChaCha20Poly1305-Entschlüsselungsinstanz mit dem Schlüssel und Nonce
    cipher = Cipher(algorithms.ChaCha20(key, nonce), mode=None, backend=default_backend()).decryptor()

    # Entschlüsseln der Daten
    plaintext = cipher.update(ciphertext) + cipher.finalize()

    # Schreiben der entschlüsselten Daten in die Ausgabedatei
    with open(output_file, 'wb') as file:
        file.write(plaintext)

with open("chkey.txt", "rb") as keyfile:
    key = keyfile.read()



for file in os.walk('encryptme/'):
    files = file[2]

for i in files:
    input_file = "encryptme/"+i
    output_file = "encryptme/"+i
    decrypt_file_chacha20(key, input_file, output_file)

