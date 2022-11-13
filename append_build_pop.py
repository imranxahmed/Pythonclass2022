# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 08:25:07 2022
@author: admin
"""
import sys

my_list = []

def list_ops():
    
    menu = '\n\n'
    menu += '**** Main Menu **** \n\n'
    menu += 'Append list: enter       "append"  \n'
    menu += 'Pop list: Enter          "pop" \n'
    menu += 'Pop at index: Enter      "select" \n'
    menu += 'Insert at Index: Enter   "insert" \n'
    menu += 'Print list: Enter        "list" \n'
    menu += 'Exit:                    "exit" or \t "quit" \n'
    print(menu, end='\n\n')

def append_list():
    
    print('type "done" to quit append function')
    while True:
    
         get_item = input('Enter anything: ')
    
    
         if get_item == 'done':
            print('list completed: \n')
            print(my_list, end='\n')
            break
         else:
            my_list.append(get_item)
    
def pop_list():  
    
    if len(my_list) == 0:
        print('Ur list is empty. Call append_list() to build one \n')
    while len(my_list) > 0:
        print('startig poping items from the list')
        print('Popping ', my_list.pop())
        print(my_list)
        
def pop_select():
    
    if len(my_list) == 0:
        print('Ur list is empty. Call append_list() to build one \n')
    
    print('\n type 100 to quit', end='\n')    
    while len(my_list) > 0:
        pop_item = int(input('what index to remove item from: '))
        
        
        if pop_item.__eq__(100):
            print('you have chosen to say goodbyes')
            sys.exit()
            
        print(my_list[pop_item])
        print('Removing: {0} '.format(my_list.pop(pop_item)))
        
        #my_list.pop(pop_item)
        print('Remaining List: {0}'.format(my_list), end='\n\n')
 
def show_list():
    
    if len(my_list) == 0:
        print('Ur list is empty. Call append_list() to build one \n')
    else:
        print('The list has {0} elements'.format(len(my_list)))
        print(my_list)
        
        
def insert_list():
    
    ask_index = input('Index please: ')
    ask_item = input('Insert Item please: ')
    
    try:
         my_list.insert(int(ask_index), ask_item)
    
    except IndexError as err:
        print('Index error: {0}'.format(err))
            

''' start calling my functions '''

def main():
    
    while True:
        
        try:
            
            list_ops()
            oper = input('Enter Operation: ')
            
            if oper.__eq__('exit') or oper.__eq__('quit'):
                
                sys.exit(0)
            
            elif oper.__eq__('append'):
                append_list()
            
            elif oper.__eq__('pop'):
                pop_list()
                
            elif oper.__eq__('select'):
                pop_select()
                
            elif oper == 'insert':
                insert_list()
                
            elif oper.__eq__('list'):
                show_list()
                
        except (IOError, InterruptedError, TypeError ):
            sys.exit('Encountered an Error, Exiting.')
            
        except SyntaxError as serr:
            file = serr.filename()
            line_num = serr.lineno()
            off_set = serr.offset()
            src_code = serr.text()
            print('serr Type: {0}'.format(type(serr)))
            print('Filename: {0} \n line-no: {1} \n offset: {2} \n source:{3}\n'.format(file, line_num, off_set, src_code))
            
            
            
            
        

''' start of Main program '''


if __name__ == "__main__":
    
    main()
