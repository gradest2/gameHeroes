FROM python:3.8-alpine3.15

COPY . /

RUN apk update &&\
    apk add binutils &&\
    pip install -r requirements.txt &&\
    pyinstaller --onefile -w -n game main.py

CMD ["sleep 3600"]
