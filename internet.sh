#!/bin/bash

/usr/local/bin/wget -q --spider --timeout=5 http://google.com

if [ $? -eq 0 ]; then
  echo "$(date) - Online" >> ~/wifi-logger/internet.log
else
  echo "$(date) - Offline" >> ~/wifi-logger/internet.log
fi

cd ~/wifi-logger && DATASET=$(python convert_statuses.py)
echo "${DATASET}" > ~/wifi-logger/dataset.json