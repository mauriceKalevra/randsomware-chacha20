from alpine:latest

RUN apk update && apk upgrade

RUN apk add python3 

#for testing, should later be automated by the attacker
RUN apk add py3-pip

RUN pip install cryptography

COPY encryptme .

CMD ["sleep", "infite"]



