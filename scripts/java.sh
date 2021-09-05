#!/bin/bash
set -e

source /data/functions.sh

CONF=$(get_conf)
JAVA_VERSION=$(echo $CONF | jq -r '.java')

apt-get -y install openjdk-${JAVA_VERSION}-jre-headless
