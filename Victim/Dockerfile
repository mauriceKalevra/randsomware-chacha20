FROM ubuntu:latest

RUN apt update && apt upgrade && apt install  openssh-server sudo -y

RUN apt install sshpass

RUN apt install python-pip

RUN pip install cryptography paramiko

RUN echo "PermitRootLogin yes">etc/ssh/sshd_config

RUN  echo 'root:root' | chpasswd

RUN service ssh start

EXPOSE 22

COPY kenndaten.py .

COPY encrypt.py .

COPY Passwords.txt .

COPY encryptme /encryptme

CMD ["/usr/sbin/sshd", "-D"]
