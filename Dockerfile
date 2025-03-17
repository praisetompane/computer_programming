FROM mcr.microsoft.com/devcontainers/python:3

WORKDIR /computer_programming

COPY . .

RUN apt-get update \
    && apt-get install aspell -y

RUN pipenv sync --system -d

RUN adduser -u 5678 --disabled-password --gecos "" computer_programming && chown -R computer_programming /computer_programming
USER computer_programming