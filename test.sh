#!/bin/bash
echo $1
python3.6 /home/XXXX/Deploy/ftp-uploader/start.py -f "$1"
read -n 1 -s
