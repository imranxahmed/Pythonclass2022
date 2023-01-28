# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 07:10:52 2023

@author: Imran Ahmed
@objective: Reading Writing Files on disk

"""
import sys, os


#boggyboggy = open("C:\\Users\\imran\\.spyder-py3\\reading-test-file.txt", mode='r', encoding='utf-8' )

def read_through(fh):
    
    for a_line in fh:
        print(a_line, end=" ")
        # if input('do u want to contine y/n: ') == 'y':
        #     continue
        # else:
        #     break
    
    if fh.closed:
        print('File handle is closed', end='\n\n')
    else:
        fh.close()

def is_textfile(filehd):
    
    '''Only interative text files return True'''
    return  filehd.isatty()

def file_menu():
    
    item = 'File Ops Menu\n'
    item += 'read: Read a File: \n'
    item += 'write: Write a File: \n'
    item += 'exit or quit \n'
    print(item)
    
def create_file():
    item = '[Unit]'
    item += 'Description=MyApp'
    item += 'After=docker.service'
    item += 'Requires=docker.service'
    item += '[Service]'
    item += 'TimeoutStartSec=0'
    item += 'ExecStartPre=-/usr/bin/docker kill busybox1'
    item += 'ExecStartPre=-/usr/bin/docker rm busybox1'
    item += 'ExecStartPre=/usr/bin/docker pull busybox'
    item += 'ExecStart=/usr/bin/docker run --name busybox1 busybox /bin/sh -c (trap exit 0)'

def write_file(fh):
    
    addition = input('What to write: ')
    fh.write(addition + '\n')
    fh.seek(0)
    for aline in fh:
        print(aline)
    fh.close()
    
    
    
#append = open('C:/Users/imran/.spyder-py3/reading-test-file.txt', mode='a+', encoding='utf-8')

#os.SEEK_CUR
#append.write('Start of class - Sunday 1/22/2023\n')

#read_through(append)

if __name__ == '__main__':
    
    file_menu()
    get_ops = input('What you would like to do: ')
    if get_ops.__eq__('read'):
        ask_file = open(input('Filename: '), mode='r+', encoding='utf-8')
        read_through(ask_file)
        
    elif get_ops.__eq__('write'):
        ask_file = open(input('Filename: '), mode='a+', encoding='utf-8')
        write_file(ask_file)
        
    elif get_ops.__eq__('exit') or get_ops.__eq__('quit'):
        sys.exit(0)

        
        
        
        
        
        
    
    
    