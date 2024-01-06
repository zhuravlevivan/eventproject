FROM python:3.10

RUN apt-get update && apt-get install -y python3-pip

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . /app

RUN python events/manage.py makemigrations --settings=events.settings --no-input

RUN python events/manage.py migrate --settings=events.settings --no-input