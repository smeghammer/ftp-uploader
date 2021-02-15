# FTP Uploader

A simple python3 application for uploading a file to an FTP server. Specifically triggered by [this Doomworld post](https://www.doomworld.com/forum/topic/118982-uploading-to-idgames-a-difficult-and-discouraging-experience/).

The main requirement was for a Drag and Drop interface. I decided that buggering about with tkinter was a rabbit hole I didn't want to disappear down, so I decided to write a CLI application and interfcae with it via desktop shortcuts and batch and shell files, depending on the platform.

---------------------------------------------
NOTE:
YOU CAN ONLY DROP ONE FILE AT A TIME
---------------------------------------------


It's essentially three components:

 - A python script and associated configuration file that does the work
 - A shell file (`.bat` or `.sh`) that accepts parameterised arguments
 - A shortcut file that accepts dragged files

## Components
 - `README.md`: This file... 
 - `start.py` Python3 script file that actually performs the FTP upload
 - `config.idgames.ini`	Configuration file. Here you add the credentials for the target FTP server. *please remove the '.idgames' part of the filename - see below*
 - `uploader.bat` Windows batch file to launch the python code. *You will need to confirm the path value in here - see below*
 - `uploader.idgames.sh` Equivalent Ubuntu (Linux) shell file. *You will need to confirm the path value in here and remove the '.idgames' part of the filename - see below*
 - `uploader.idgames.desktop` Ubuntu `.desktop` file for dropping a file. *You will need to confirm the path value in here and remove the '.idgames' part of the filename - see below*
 
## Requirements
 - **Python3**: Ubuntu has this by default. You will need to install on Windows from [here](https://www.python.org/downloads/windows/)
 
The packages imported into the code (`argparse`, `configparser`, `ftplib` and `os`) are all part of the default installation of Python3 and you should not need to install these separately.

## Setup
1: Clone or download from the repository
2: **Rename** the files that include `.idgames` by removing this:

On Windows, this file:
 - `config.idgames.ini` --> `config.ini`

Additionally, on Ubuntu:
 - `uploader.idgames.desktop` --> `uploader.desktop`
 - `uploader.idgames.sh` --> `uploader.sh`

### General
The renamed `config.ini` needs to be updated to include your email as the `pass=` value.

All other values should be OK for uploading to the IDGames archive.

### Windows
1: Install Python 3 from [here](https://www.python.org/downloads/windows/). Once done, check that you can open a python CLI prompt by typing `python` in a terminal window. If you get a bunch of text indicating the python version, then you are good to go (note it may have installed as `python3` if python2 is already installed). 
2: Make sure you amend the batch file to use the correct python alias (`python` most likely) and the path bit (before `\start.py -f "%1"`) to wherever you deployed the code 
3: Create a desktop shortcut to the batch file. Drag/drop while **right-clicking**, or rt-click, and select 'new shortcut'.

### Ubuntu
1: Amend the renamed `uploader.sh` such that the `WORKING_DIRECTORY` variable points to the location you downloaded the code into.
2: You may need to amend the python alias if you have changed the python3 default alias to something else
3: Amend the renamed `uploader.desktop` property `Exec=` value to reflect your deployment location. **DO NOT** remove the `/uploader.sh %U` at the end!


