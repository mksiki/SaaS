FROM python

ENV PYTHONUNBUFFERED 1

ENV PYTHONDONTWRITEBYTECODE 1

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt 

COPY . . 