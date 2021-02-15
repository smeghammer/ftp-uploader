#!/bin/bash

# define where your deployment is:
WORKING_DIRECTORY=/path/to/location/ftp-uploader/

#echo the passed filename:
echo $1

#change shell file execution context to the directory in which the uploader is deployed:
cd $WORKING_DIRECTORY

#Add your python3 alias here:
python3 ${WORKING_DIRECTORY}start.py -f "$1"

#wait for a keypress to exit (you can comment this if you want):
echo "Press any key to exit"
read -n 1 -s
