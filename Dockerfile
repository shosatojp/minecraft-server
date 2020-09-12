FROM alpine:3.12
ARG VERSION

RUN apk update && \
    apk add openjdk8-jre

WORKDIR /data
COPY ./versions.txt .
RUN cat versions.txt | grep -E "^${VERSION} " | head -1 | awk '{print $2}' > url.txt
RUN wget -O download.jar `cat url.txt`
RUN if [ "$(echo `cat url.txt` | grep installer)" ];then    \
        java -jar download.jar nogui -installServer;        \
        mv minecraft_server.*.jar server.jar;               \
    else                                                    \
        mv download.jar server.jar;                         \
    fi

WORKDIR /home
CMD java -Xms${Xms} -Xmx${Xmx} -jar /data/server.jar nogui
EXPOSE 25565
