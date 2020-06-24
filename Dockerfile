FROM python:3.8
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements.txt /code/requirements.txt
COPY app /code/app
COPY config.py /code/config.py
COPY tinyurl.py /code/tinyurl.py
COPY tests /code/tests

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

