FROM alpine:3.12
ARG VERSION

RUN apk update && \
    apk add openjdk8-jre

WORKDIR /data
COPY ./versions.txt .
RUN wget -O server.jar "$(cat versions.txt | grep -E "^${VERSION} " | head -1 | awk '{print $2}')"
RUN if [ "$(echo $VERSION | grep forge)" ];then                                                             \
        wget -O installer.jar "$(cat versions.txt | grep -E "^${VERSION} " | head -1 | awk '{print $3}')";  \
        java -jar installer.jar nogui -installServer;                                                       \
        rm installer.jar;                                                                                   \
    fi

WORKDIR /home
CMD mkdir -p world && \
    java -Xms${Xms} -Xmx${Xmx} -jar /data/server.jar nogui
EXPOSE 25565
