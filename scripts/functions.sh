#!/bin/bash

function get_conf() {
    echo $(cat /data/versions.json | jq ".[] | select(.version == \"$VERSION\")")
}
