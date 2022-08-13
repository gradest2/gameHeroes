FROM python:3.8-alpine3.15

COPY . /

RUN apk update &&\
    apk add binutils &&\
    pip install -r requirements.txt &&\
    pyinstaller --onefile --noconfirm --console --name "gameHeroes" --add-data 'data.yaml:data.yaml' main.py

CMD ["/dist/gameHeroes"]
