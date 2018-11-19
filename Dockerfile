FROM python:3.6

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /code
COPY . /code/
RUN pip install -r /code/requirements.txt

WORKDIR /code/backend/djangorest

EXPOSE 8000
