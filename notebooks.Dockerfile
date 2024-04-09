FROM ubuntu:latest

RUN apt-get update

RUN apt-get install -y python3 &&\
    apt-get install -y python3-pip

RUN pip3 install pandas matplotlib ipympl pyvis

RUN pip3 install notebook jupyterlab

# Not recommended, but makes it easier to share python code between folders for the current use
ENV PYTHONPATH="${PYTHONPATH}:/algorithms-workshop"


COPY /theory /algorithms-workshop

VOLUME /algorithms-workshop

WORKDIR /algorithms-workshop