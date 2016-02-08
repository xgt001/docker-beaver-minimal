#!/bin/sh
python -c 'import boto'
is_boto_installed=`echo $?`
[ $is_boto_installed -ne 0 ] && { easy_install boto; }
python get_queue.py
echo "Triggering Docker build"
docker build -f Dockerfile -t docker-beaver .
