# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 08:25:07 2022

@author: admin
"""
import sys

my_list = []

def list_ops():
    
    menu = '\n\n'
    menu += '\u2139 \u2588 Main Menu \u2588 \u2139 \n\n'
    menu += '\u2588 Append list: enter      \u2588   "append"  \n'
    menu += '\u2588 Pop list: Enter         \u2588   "pop" \n'
    menu += '\u2588 Pop at index: Enter     \u2588   "select" \n'
    menu += '\u2588 Insert at Index: Enter  \u2588   "insert" \n'
    menu += '\u2588 Positive Index: Enter   \u2588   "pindex" \n'
    menu += '\u2588 Negative Index: Enter   \u2588   "nindex" \n'
    menu += '\u2588 Print list: Enter       \u2588   "list" \n'
    menu += '\u2139 Exit: \u2139   Enter   \u2588 "exit" \u2588 or \u2588 "quit" \u2588 \n'
    print(menu, end='\n\n')

def append_list():
    while True:
    
         get_item = input('Enter anything: ')
    
    
         if get_item == 'done':
            print('list completed: \n')
            print(my_list, end='END-OF-LINE\n')
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
    
    while len(my_list) > 0:
        pop_item = int(input('what index to remove item from: '))
        if pop_item.__eq__('exit'):
            sys.exit()
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

def negative_index():
    
    print('\n\n')
    print('Negative Index in Python', end='\n')
    for jim in iter(my_list[::-1]):
        print('index: {0}'.format(my_list.index(jim)))
        
def positive_index():
    
    print('\n\n')
    print('Positive Index in Python', end='\n')
    for jim in iter(my_list):
        print('index: {0}'.format(my_list.index(jim)))

''' above both functions NOT added Yet'''           

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
                
            elif oper.__eq__('nindex'):
                negative_index()
            
            elif oper.__eq__('pindex'):
                positive_index()
                
                
                
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