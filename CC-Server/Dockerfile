FROM ubuntu:latest

RUN apt update && apt upgrade -y 

RUN apt install  openssh-server -y

RUN apt install sshpass -y 

RUN apt install python3-pip -y

WORKDIR /

COPY makekey.py decrypt.py senddecryption.py /

RUN pip install cryptography paramiko

RUN echo "PermitRootLogin yes">etc/ssh/sshd_config

RUN  echo 'root:root' | chpasswd

RUN service ssh start

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]
