FROM mcr.microsoft.com/devcontainers/python:3.13 AS python

WORKDIR /computer_programming

COPY . .
    
RUN pipenv install

FROM sbtscala/scala-sbt:eclipse-temurin-17.0.4_1.7.1_3.2.0 AS scala