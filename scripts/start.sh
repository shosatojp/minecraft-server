#!/bin/bash
set -e

CONF=$(cat /data/versions.json | jq ".[] | select(.version == \"$VERSION\")")
TYPE=$(echo $CONF | jq -r '.type')

cd /home/
mkdir -p world
JAVA_OPTIONS="${Xms:+-Xms$Xms} ${Xmx:+-Xmx$Xmx}"

echo "eula=$eula" > eula.txt

case $TYPE in
    vanilla)
        java $JAVA_OPTIONS -jar /data/server.jar nogui
        ;;
    forge-universal)
        java $JAVA_OPTIONS -jar /data/universal.jar nogui
        ;;
    forge-installer)
        java $JAVA_OPTIONS -jar /data/forge-*.jar nogui
        ;;
    forge-run)
        cp -r /data/* /home/
        echo "$JAVA_OPTIONS" > user_jvm_args.txt
        ./run.sh
        ;;
esac