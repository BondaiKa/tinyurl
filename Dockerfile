FROM python:3
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements.txt /code/requirements.txt
COPY app /code/app
#COPY bin /code/bin
COPY config.py /code/config.py
COPY app.py /code/app.py

RUN mkdir -p /code/var

RUN pip install -r requirements.txt

CMD python app.py
