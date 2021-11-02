FROM ubuntu:latest
MAINTAINER saifnaqviit3019@gmail.com
RUN apt-get update 
RUN apt-get install -y software-properties-common 
RUN apt-add-repository ppa:ansible/ansible $ sudo apt-get update 
RUN apt-get install -y ansible
