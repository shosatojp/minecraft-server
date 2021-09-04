FROM ubuntu:20.04
ARG VERSION

RUN apt-get update && \
    apt-get -y install openjdk-16-jre wget

WORKDIR /data
COPY ./versions.txt .
RUN wget -O installer.jar "$(cat versions.txt | grep -E "^${VERSION} " | head -1 | awk '{print $2}')"
RUN java -jar installer.jar nogui --installServer
COPY ./start-run.sh .


WORKDIR /home
CMD sleep 100000000
CMD mkdir -p world && \
    cp -r /data/* /home/ && \
    ./start-run.sh
EXPOSE 25565
