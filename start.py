'''
Created on 9 Jan 2021

@author: smeghammer

see https://www.devdungeon.com/content/python-ftp-client-tutorial#toc-16
'''
import argparse
import configparser
from ftplib import FTP
import os


'''
capture CLI args:
'''
parser = argparse.ArgumentParser(description='Simple FTP uploader')
parser.add_argument( '-f', '--file', help='file to upload (single file only)', type=str, required=True)
args = parser.parse_args()

def upload(file):
    print("starting...")
    try:
        print("trying...")
        config = configparser.RawConfigParser()
        config.sections()
        config.read('config.ini') #this will fail if no config.ini found
        print("config read OK")
        '''
        Instantiate FTP instance with target and credentials; and set target path:
        '''
        print(config)
        ftp = FTP(config['ftp']['target'], config['user']['login'], config['user']['pass'])
        print(ftp)
        ftp.cwd(config['ftp']['path'])
        print(ftp)
        
        res = ftp.retrlines('LIST')
        print(res)
        #text mode
        try:
            text_file = open(file, 'rb')
            #TODPO: intercept here if no input file found:
    #         ftp.storlines('STOR '+file, text_file)
            print(file.split('\\')[-1])
            '''
            Split the filepath to extract the actual file. Note: OS independent:
            '''
            ftp.storbinary('STOR '+file.split(os.path.sep)[-1], text_file)
        except FileNotFoundError as err:
            print('input file not found: {0}'.format(str(err)))
        except Exception as err:
            print('an ftp error occurred: {0}'.format(str(err)))
        
        finally:
            ftp.quit()
    except FileNotFoundError as err:
        print('no config file found! ({0})'.format(str(err)))
    except Exception as err:
        print('a general error occurred: {0}'.format(str(err)))
    
    finally:
        print("Done")

'''
Entry point:
'''
if __name__ == '__main__':
    print('starting with ' + args.file)
    
    ''' call upload function with file path '''
    upload(args.file)
    
