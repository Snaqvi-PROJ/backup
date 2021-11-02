FROM fedora:latest
MAINTAINER "saifnaqviit3019@gmail.com"
RUN yum install -y rpm-build
RUN yum install -y rpmdev-setuptree
RUN yum install -y rpmdevtools
