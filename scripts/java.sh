#!/bin/bash
set -e

CONF=$(cat /data/versions.json | jq ".[] | select(.version == \"$VERSION\")")
JAVA_VERSION=$(echo $CONF | jq -r '.java')

apt-get -y install openjdk-${JAVA_VERSION}-jre
