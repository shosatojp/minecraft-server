FROM ubuntu:18.04
RUN apt-get update && apt-get install -y wget openjdk-8-jdk
RUN mkdir minecraft && wget -O minecraft/minecraft_server.jar \
https://s3.amazonaws.com/Minecraft.Download/versions/1.10.2/minecraft_server.1.10.2.jar
RUN echo "eula=true" > eula.txt
CMD java -Xms4096m -Xmx4096m -jar minecraft/minecraft_server.jar nogui
EXPOSE 25565