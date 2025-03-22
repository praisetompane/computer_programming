FROM mcr.microsoft.com/devcontainers/base:bookworm

WORKDIR /computer_programming

COPY . .

RUN apt-get update \
    && apt-get install aspell -y

RUN apt-get install python3 -y && apt-get install python3-pip -y && apt-get install pipenv -y && ln -s /usr/bin/python3 /usr/bin/python
RUN apt-get install ghc -y

RUN adduser -u 5678 --disabled-password --gecos "" computer_programming && chown -R computer_programming /computer_programming
USER computer_programming