#FROM docker/whalesay:latest
FROM ubuntu:18.04
RUN apt-get -y update && apt-get install -y cowsay fortunes
#CMD /usr/games/fortune -a | cowsay
# LABEL about the custom image
LABEL maintainer="@geo_Inca"
LABEL version="0.1.1"
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
                   iputils-ping wget git gzip 
RUN apt install -y software-properties-common                   
RUN apt install -y net-tools                   
RUN apt install -y python3 python3-pip python3-dev
RUN apt install -y texinfo
RUN wget https://dl.min.io/client/mc/release/linux-amd64/mc
RUN chmod +x mc
RUN cp mc /usr/local/bin 
RUN ln -s /usr/games/cowsay /usr/local/bin/cowsay
WORKDIR /app
RUN echo "alias tuxsay=\"cowsay -f tux \"" >> ~/.bashrc
#RUN source  ~/.bashrc
#RUN pip install --upgrade pip
RUN pip3 install text_to_image

#CMD ["/usr/games/cowsay", "Dockerfiles are cool!"]