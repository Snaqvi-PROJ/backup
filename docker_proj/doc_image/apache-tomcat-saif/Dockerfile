FROM ubuntu

RUN apt-get update

RUN apt-get install openjdk-8-jdk -y

RUN mkdir -p /usr/local/apache-tomcat

COPY apache-tomcat /usr/local/apache-tomcat

ENV CAT_HOME=/usr/local/apache-tomcat/bin/startup.sh

ENTRYPOINT  /usr/local/apache-tomcat/bin/startup.sh && /bin/bash
