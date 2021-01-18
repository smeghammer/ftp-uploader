#!/bin/bash
echo $1
python3.6 /home/silas/Deploy/ftp-uploader/FTP\ Uploader/start.py -f "$1"
read -n 1 -s
