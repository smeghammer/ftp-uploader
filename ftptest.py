'''
Created on 17 Jan 2021

@author: smegh
'''
from ftplib import FTP

def test():
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
    
    ftp.quit()


if __name__ == "__main__":
    test()