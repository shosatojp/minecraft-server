#!/bin/bash
set -e

source /data/functions.sh

CONF=$(get_conf)
TYPE=$(echo $CONF | jq -r '.type')
SERVER=$(echo $CONF | jq -r '.server')
INSTALLER=$(echo $CONF | jq -r '.installer')
UNIVERSAL=$(echo $CONF | jq -r '.universal')

case $TYPE in
    vanilla)
        wget -O server.jar $SERVER
        ;;
    forge-universal)
        wget -O installer.jar $INSTALLER
        wget -O universal.jar $UNIVERSAL
        java -jar installer.jar nogui --installServer
        rm installer.jar
        ;;
    forge-installer)
        wget -O installer.jar $INSTALLER
        java -jar installer.jar nogui --installServer
        rm installer.jar
        ;;
    forge-run)
        wget -O installer.jar $INSTALLER
        java -jar installer.jar nogui --installServer
        rm installer.jar
        ;;
    fabric)
        wget -O installer.jar $INSTALLER
        java -jar installer.jar server -mcversion ${VERSION#fabric-} -downloadMinecraft
        rm installer.jar
        mv server.jar vanilla.jar
        mv fabric-server-launch.jar server.jar
        echo "serverJar=vanilla.jar" > fabric-server-launcher.properties
        ;;
esac
