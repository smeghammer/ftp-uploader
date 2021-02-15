# FTP Uploader

A simple python3 application for uploading a file to an FTP server. Specifically triggered by [this Doomworld post](https://www.doomworld.com/forum/topic/118982-uploading-to-idgames-a-difficult-and-discouraging-experience/).

The main requirement was for a Drag and Drop interface. I decided that buggering about with tkinter was a rabbit hole I didn't want to disappear down, so I decided to write a CLI application and interfcae with it via desktop shortcuts and batch and shell files, depending on the platform.

It's essentially three components:

 - A python script and associated configuration file that does the work
 - A shell file (`.bat` or `.sh`) that accepts parameterised arguments
 - A shortcut file that accepts dragged files

## Components
 - `README.md`: This file... 
 - `start.py`		Python3 script file that actually performs the FTP upload
 - `config.idgames.ini`	Configuration file. Here you add the credentials for the target FTP server. *please remove the '.idgames' part of the filename - see below*
 - `uploader.bat` Windows batch file to launch the python code. *You will need to confirm the path value in here - see below*
 - `uploader.idgames.sh` Equivalent Ubuntu (Linux) shell file. *You will need to confirm the path value in here and remove the '.idgames' part of the filename - see below*
 - `uploader.idgames.desktop` Ubuntu `.desktop` file for dropping a file. *You will need to confirm the path value in here and remove the '.idgames' part of the filename - see below*
 - `uploader.lnk` Equivalent Windows desktop shortcut file.
 
 
## Requirements


## Setup
