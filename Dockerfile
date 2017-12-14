FROM ubuntu

MAINTAINER Alex woodhouse <alexander.woodhouse@perfect.com>

RUN apt-get update; apt-get -y install python-software-properties software-properties-common curl git python3-pip;python3 -m pip install --upgrade pip;python3 -m pip install slackclient;

COPY src /opt/slack
WORKDIR /opt/slack
