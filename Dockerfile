FROM python:3.10
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir /chat_app
WORKDIR /chat_app

COPY requirements.txt /chat_app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ADD . /chat_app/
