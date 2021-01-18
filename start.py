'''
Created on 9 Jan 2021

@author: smegh

see https://www.devdungeon.com/content/python-ftp-client-tutorial#toc-16
'''
import argparse
import importlib
from ftplib import FTP


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
    # ftp = FTP('archives.gamers.org','anonymous','smeghammer@live.com')
    # ftp.cwd('pub/idgames/incoming')
    
    '''
    local
    '''
    ftp = FTP('192.168.1.106','silas','%Asteroth666%')
    ftp.cwd('/home/silas/ftp')
    #/home/silas/Documents
    
    # ftp.cwd('Documents')
    
    res = ftp.retrlines('LIST')
    
    #text mode
    with open(file, 'rb') as text_file:
#         ftp.storlines('STOR '+file, text_file)
        ftp.storbinary('STOR '+file, text_file)
    
    
    ftp.quit()

'''
Entry point:
'''
if __name__ == '__main__':
    print('starting with ' + args.file)
    
    ''' Here I load a crawler based on the passed arg:  '''
    test(args.file)
    
