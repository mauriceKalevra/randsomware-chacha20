from alpine:latest

RUN apk update && apk upgrade

RUN apk add python3 

RUN apk add py3-pip

RUN pip install cryptography  

RUN mkdir Importand_Data

RUN mkdir Pictures

RUN touch personal.txt

RUN touch Passworts.txt 

COPY encryptme/ .

CMD ["sleep", "infite"]



