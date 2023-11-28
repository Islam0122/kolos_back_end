FROM python:3.9

ENV PYTHONWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

WORKDIR /app

COPY ./requirements/req.txt /app/requirements/

RUN pip install --upgrade pip

RUN pip install -r requirements/req.txt

COPY . /app