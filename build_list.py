# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 07:06:49 2022

@author: Imran Ahmed - build a list

"""


if __name__ == "__main__":
    item_list = []

while True:
    
    try:
        ask_user = input('Your input Please: ')
        if ask_user == 'exit':
            print('Input is complete...')
            print('The list has {0} elements.\n'.format(len(item_list)))
            print('The list is:\n', item_list)
            break 
            ''' this will exit the LOOP '''

        else:
            item_list.append(ask_user) 
            print('Data Type is: ', type(ask_user))
            print('The list is \n', item_list)
        
    except TypeError as e:
        print('A Type Error Occured: {0} '.format(e))
        break
        
    except KeyboardInterrupt as e:
        print('User Interrupt Error: {0} '.format(e))
        break
    
    except SyntaxError as e:
        print('Found Syntax Error:'.format(e))
        break           
    
