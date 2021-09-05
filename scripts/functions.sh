#!/bin/bash

function get_conf() {
    case $LOADER in
        vanilla)
            echo $(cat /data/versions.json | jq ".[] | select(.version == \"$VERSION\")")
            ;;
        forge)
            echo $(cat /data/versions.json | jq ".[] | select(.version == \"$LOADER-$VERSION\")")
            ;;
        fabric)
            echo $(cat /data/versions.json | jq ".[] | select(.version == \"$LOADER\")")
            ;;
    esac
}
