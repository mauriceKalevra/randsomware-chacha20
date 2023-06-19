from alpine:latest

RUN apk update && apk upgrade

RUN apk add python3 

RUN apk add py3-pip

RUN pip install cryptography  

COPY Passwords.txt .

COPY encryptme /encryptme

CMD ["sleep", "infite"]



