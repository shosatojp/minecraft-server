FROM openjdk:8-jre

ARG VERSION
COPY ./versions.txt /
RUN wget -O /server.jar \
    $(cat /versions.txt | grep -E "^${VERSION} " | head -1 | awk '{print $2}')

WORKDIR /home
CMD java -Xms${Xms} -Xmx${Xmx} -jar /server.jar nogui
EXPOSE 25565
