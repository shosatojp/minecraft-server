#!/bin/bash
echo "-Xms${Xms} -Xmx${Xmx}" > user_jvm_args.txt
./run.sh
