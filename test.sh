#!/bin/bash

function test_version() {
    VERSION=$1

    TAG=minecraft-server:$VERSION
    NAME=minecraft-server-test-$VERSION

    docker build --build-arg VERSION=$VERSION -t $TAG .
    docker kill $NAME
    docker rm $NAME
    docker run -d --name $NAME -p 127.0.0.1:25565:25565 -e eula=true $TAG

    echo "=== waiting for server start up ==="

    for i in `seq 1 60`;do
        sleep 3

        echo "=== checking for server start up: $i ==="
        mcstatus localhost:25565 status

        if [[ $? == 0 ]];then
            echo "=== server correctly started up ==="
            echo "=== terminating container ==="
            docker kill $NAME
            docker rm $NAME
            docker rmi $TAG
            exit 0
        fi
    done

    exit 1
}

if [[ "$1" == "" ]];then
    echo "First argument must be a version"
    exit 1
fi

test_version $1