FROM alpine:3.12
ARG VERSION

RUN apk update && \
    apk add openjdk8-jre

COPY ./versions.txt /
RUN wget -O /server.jar \
    $(cat /versions.txt | grep -E "^${VERSION} " | head -1 | awk '{print $2}')

WORKDIR /home
CMD java -Xms${Xms} -Xmx${Xmx} -jar /server.jar nogui
EXPOSE 25565
