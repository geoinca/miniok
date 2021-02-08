FROM python:3.6.7

RUN apt-get update && apt-get upgrade -y

RUN apt-get install -y build-essential python3 python3-pip python3-dev git swig

RUN pip install --upgrade pip

ADD ./requirements.txt /app/requirements.txt

WORKDIR /app
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

# NOTE: including ConfigSpace in requirements make a lot of problem

COPY ./setup.py /app
COPY ./countobj.py /app
COPY ./countobj01.py /app
RUN pip3 install .
