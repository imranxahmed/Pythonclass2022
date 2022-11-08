# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 08:25:07 2022

@author: admin
"""
import sys

my_list = []

def list_ops():
    
    menu = '\n\n'
    menu += 'append: Append to a list \n'
    menu += 'pop: pop an item from Top of the list \n'
    menu += 'select: pop an item at index  \n'
    menu += 'insert: Insert at Index value \n'
    print(menu, end='\n')

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
        
def pop_select():
    
    while len(my_list) > 0:
        pop_item = int(input('what index to remove item from: '))
        if pop_item.__eq__('exit'):
            sys.exit()
        print('Removing: {0} '.format(my_list.pop(pop_item)))
        
        #my_list.pop(pop_item)
        print('Remaining List: {0}'.format(my_list), end='\n\n')
        
def insert_list():
    
    ask_index = input('Index please: ')
    ask_item = input('Insert Item please: ')
    
    try:
         my_list.insert(int(ask_index), ask_item)
    
    except IndexError as err:
        print('Index error: {0}'.format(err))
            

''' start calling my functions '''

''' start of Main program '''

def main():
    
    try:
        
        list_ops()
        oper = input('Enter Operation: ')
        
        if oper.__eq__('append'):
            append_list()
        
        elif oper.__eq__('pop'):
            pop_list()
            
        elif oper.__eq__('select'):
            pop_select()
            
        elif oper == 'insert':
            insert_list()
            
    except (IOError, InterruptedError, TypeError ):
        sys.exit('Encountered an Error, Exiting.')
    
if __name__ == "__main__":
    
    main()