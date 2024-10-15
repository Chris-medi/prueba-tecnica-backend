FROM python:3.12-bookworm
RUN mkdir /app
WORKDIR /app

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN apt-get update
RUN apt-get install gcc libsm-dev ffmpeg libxext-dev -y

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 80
