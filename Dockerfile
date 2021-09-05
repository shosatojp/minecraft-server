FROM ubuntu:20.04

RUN apt-get update && \
    apt-get -y install wget jq

ARG VERSION
ENV VERSION=$VERSION

WORKDIR /data
COPY ./versions.json .

# install jre
COPY ./scripts/java.sh .
RUN /data/java.sh

# install minecraft server
COPY ./scripts/install.sh .
RUN /data/install.sh

COPY ./scripts/start.sh .
WORKDIR /home
CMD /data/start.sh

EXPOSE 25565
