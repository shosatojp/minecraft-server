#!/bin/bash
function build_version() {
    VERSION=$1
    REPO=$2
    TAG=$REPO:$VERSION

    docker build --build-arg VERSION=$VERSION -t $TAG .
    docker push $TAG
}

REPO=shosatojp/minecraft-server
VERSIONS=(
    1.17.1 
    forge-1.17.1
    fabric-1.17.1
    1.16.5
    forge-1.16.5
    fabric-1.16.5
    forge-1.12.2
    forge-1.7.10
    forge-1.6.4
)

for version in ${VERSIONS[@]};do
    echo "=== building version: $version ==="
    build_version $version $REPO
done