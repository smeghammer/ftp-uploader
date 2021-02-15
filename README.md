# FTP Uploader

A simple python3 application for uploading a file to an FTP server. Specifically triggered by [this Doomworld post](https://www.doomworld.com/forum/topic/118982-uploading-to-idgames-a-difficult-and-discouraging-experience/).

The main requirement was for a Drag and Drop interface. I decided that buggering about with tkinter was a rabbit hole I didn't want to disappear down, so I decided to write a CLI application and interfcae with it via desktop shortcuts and batch and shell files, depending on the platform.

## Components
 - `start.py`		Python3 script file that actually performs the FTP upload
 - `config.ini`	Configuration file. Here you add the credentials for the target FTP server

## Requirements


## Setup
