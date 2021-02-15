#!/bin/bash

#echo the passed filename:
echo $1

#pwd
#change to the directory in which the uploader is deployed:
cd /home/silas/Deploy/ftp-uploader/

#Add your python3 alias here:
python3.6 /home/silas/Deploy/ftp-uploader/start.py -f "$1"

#wait for a keypress to exit (you can comment this if you want):
read -n 1 -s
