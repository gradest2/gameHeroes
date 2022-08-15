FROM python:3.8-bullseye

COPY . /

RUN apt-get -y update &&\
    apt-get -y install binutils &&\
    pip install -r requirements.txt &&\
    pyinstaller --onefile --noconfirm --console --name "gameHeroes" --add-data '/data.yaml:data.yaml' main.py

CMD ["/dist/gameHeroes"]
