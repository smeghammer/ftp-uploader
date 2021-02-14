'''
Created on 9 Jan 2021

@author: smeghammer

see https://www.devdungeon.com/content/python-ftp-client-tutorial#toc-16
'''
import argparse
import importlib
from ftplib import FTP
import os


'''
capture CLI args:
'''
parser = argparse.ArgumentParser(description='Start metadata collection with startnode, db server, db port and DB name')
# Required args:
parser.add_argument( '-f', '--file', help='file to upload', type=str, required=True)
args = parser.parse_args()

def test(file):
    print(file)
    
    '''
    for ID Games:
    '''
    ftp = FTP('archives.gamers.org','anonymous','your_email@your_host.com')
    ftp.cwd('pub/idgames/incoming')
    

    
    res = ftp.retrlines('LIST')
    print(res)
    #text mode
    with open(file, 'rb') as text_file:
#         ftp.storlines('STOR '+file, text_file)
        print(file.split('\\')[-1])
        ftp.storbinary('STOR '+file.split(os.path.sep)[-1], text_file)
 
    ftp.quit()

'''
Entry point:
'''
if __name__ == '__main__':
    print('starting with ' + args.file)
    
    ''' Here I load a crawler based on the passed arg:  '''
    test(args.file)
    
