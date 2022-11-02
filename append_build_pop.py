# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 08:25:07 2022

@author: admin
"""

my_list = []


def append_list():
    while True:
    
         get_item = input('Enter anything: ')
    
    
         if get_item == 'exit':
            print('list completed: \n')
            print(my_list, end='end-of-line\n')
            break
         else:
            my_list.append(get_item)
    
def pop_list():    
    while len(my_list) > 0:
        print('startig poping items from the list')
        print('Popping ', my_list.pop())
        print(my_list)

''' start calling my functions '''

''' start of Main program '''

if __name__ == "__main__":
    
    append_list()
    pop_list()

