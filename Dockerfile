FROM python:3.8
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements.txt /code/requirements.txt
COPY app /code/app
COPY config.py /code/config.py
COPY app.py /code/app.py

RUN pip install -r requirements.txt

CMD python app.py
