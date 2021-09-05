#!/bin/bash
set -e

CONF=$(cat /data/versions.json | jq ".[] | select(.version == \"$VERSION\")")
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
        ;;
esac