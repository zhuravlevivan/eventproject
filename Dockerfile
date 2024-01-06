FROM python:3.10

RUN apt-get update && apt-get install -y python3-pip

WORKDIR /gen

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .
