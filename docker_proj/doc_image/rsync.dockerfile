FROM ubuntu
MAINTAINER "saifnaqviit3019@gmail.com"

RUN apt-get update
RUN apt-get install -y rsync
RUN apt-get clean

