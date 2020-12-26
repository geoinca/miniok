
# Download base image ubuntu 18.04
FROM ubuntu:18.04

# LABEL about the custom image
LABEL maintainer="@geo_Inca"
LABEL version="0.1"
LABEL description="This is custom Docker Image for \
test Services."
# Disable Prompt During Packages Installation
ARG DEBIAN_FRONTEND=noninteractive

# Update Ubuntu Software repository
RUN apt update

# Install nginx, php-fpm and supervisord from ubuntu repository
RUN apt install -y build-essential libssl-dev zlib1g-dev libncurses5-dev \
                   libncursesw5-dev libreadline-dev libsqlite3-dev libgdbm-dev \
                   libdb5.3-dev libbz2-dev libexpat1-dev liblzma-dev tk-dev libffi-dev \
                   iputils-ping wget
RUN apt install -y net-tools                   
RUN apt install -y python3.6

RUN wget https://dl.min.io/client/mc/release/linux-amd64/mc
RUN chmod +x mc
