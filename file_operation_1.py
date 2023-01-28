# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 07:10:52 2023

@author: Imran Ahmed
@objective: Reading Writing Files

"""
import sys, os


filehd = open("C:\\Users\\imran\\.spyder-py3\\reading-test-file.txt", mode='r', encoding='utf-8' )

def read_through(fhandle):
    
    for a_line in fhandle:
        print(a_line, end=" ")
        # if input('do u want to contine y/n: ') == 'y':
        #     continue
        # else:
        #     break
    
    if fhandle.closed():
        print('File handle is closed', end='\n\n')
    else:
        fhandle.close()

def is_textfile(filehd):
    
    '''Only interative text files return True'''
    return  filehd.isatty()

    
# [Unit]
# Description=MyApp
# After=docker.service
# Requires=docker.service
# [Service]
# TimeoutStartSec=0
# ExecStartPre=-/usr/bin/docker kill busybox1
# ExecStartPre=-/usr/bin/docker rm busybox1
# ExecStartPre=/usr/bin/docker pull busybox
# ExecStart=/usr/bin/docker run --name busybox1 busybox /bin/sh -c "trap 'exit 0' INT TERM; while true; do echo Hello World; sleep 1; done"


append = open('C:/Users/imran/.spyder-py3/reading-test-file.txt', mode='a+', encoding='utf-8')

os.SEEK_CUR
append.write('Start of class - Sunday 1/22/2023\n')

read_through(append)

