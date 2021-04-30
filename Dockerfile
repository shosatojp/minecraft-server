FROM alpine:3.12
ARG VERSION

RUN apk update && \
    apk add openjdk8-jre

WORKDIR /data
COPY ./versions.txt .
RUN JAR="$(cat versions.txt | grep -E "^${VERSION} " | head -1 | awk '{print $2}')"
RUN if [ "$(echo $VERSION | grep forge)" ];then\
        wget -O installer.jar $JAR;\
        java -jar installer.jar nogui -installServer ./server.jar; \
        rm installer.jar;\
    else \
        wget -O server.jar $JAR \
    fi

WORKDIR /home
CMD mkdir -p world && \
    java -Xms${Xms} -Xmx${Xmx} -jar /data/server.jar nogui
EXPOSE 25565