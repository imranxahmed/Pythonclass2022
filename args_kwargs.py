# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 21:46:06 2022

@author: admin
Objective: *args & *kwargs. Packing and unpacking 
Reference: https://www.shecancode.io/blog/unpacking-function-arguments-in-python
"""
'''
Unpacking: 
    During function call, we can unpack 
    python list/tuple/range/dict and pass it as separate arguments. 
      * is used for unpacking positional arguments. ** is used for unpacking keyword arguments 

Packing: 
    You might have seen *args and **kwargs in a 
    python function definition. What does that mean? It’s known as packing, 
    which packs all the arguments in a tuple. If we don’t know the number 
    of arguments to be passed during the function call, we can use packing. 

Object: Everything in python is an object.
 
    An object is characterised by its identity, its type, and its contents

Immutable types: the type of object can't be changed.
    
    strings: are immutable.  
'''

import sys


def arg_facts():
    
    menu = '\t \nThese are facts about packing/unpacking args & keyword-args \n\n'
    menu += '\t \u2139 When args are tuple, list or range as args \n'
    menu += '\t \u2139 function is DEFINED with fixed num of args \n'
    menu += '\t \u2139 TypeError: is raised if  missing required positional args \n'
    menu += '\t \u2139 function is DEFINED with arbitrary num of args *args \n'
    menu += '\t \u2139 function can be CALLED with fixed num of args \n'
    menu += '\t \u2139 function can be CALLED with arbitrary num of args *args \n'
    menu += '\t \u2139 when args are dict, unpack them during the func() call using the ** operator. \n'
    print(menu, end='\n')
    
    
def packing_tuple(func_tuple):
       
    if func_tuple is a_tuple:
        print('Inside func tuple at: {0} is Same as tuple in main: {1}'.format(id(func_tuple), id(a_tuple)), end='\n\n')
    else:
        print('Inside func Object: {0} is DIFFERENT from main func object: {1}'.format(id(func_tuple), id(a_tuple)), end='\n\n')

    
def packing_list(func_list):
    
    if func_list is a_list:
        print('Inside func Object: {0} is same LIST:{1} Object'.format(id(func_list), id(a_list)), end='\n\n')
    else:
        print('Inside func tuple {0} are NOT same LIST {1}'.format(id(func_list), id(a_list)), end='\n\n')
    
def packing_dict(func_dict):
    
    if func_dict is a_dict:
        print('Inside func dict {0} Object is same as main func dict:{1}'.format(id(func_dict), id(a_dict)), end='\n\n')
    else:
        print('Inside func dict {0} and main funct dict {1} Ojbect are NOT same'.format(id(func_dict), id(a_dict)), end='\n\n')

    
def passing_dict(abc):
    
    if abc is user_dict:
        print('Inside func dict: {0} is SAME object as user_dict object: {1}'.format(id(abc), id(user_dict)), end='\n\n')

    
    

if __name__ == "__main__":
    
    #print('local space {0}'.format(locals()))
    try:
        
        
        a_tuple = ( 13, 'form', 'life', 'check', 'tubple', 'example', 34.242 )
        a_list = [x for x in a_tuple]
        a_dict = { 'life': 'should live', 'love': 'be careful', 'chance': 'take', 'world': 'is unknown', 'happiness': 'eternal bliss'}
        user_dict = {
            
            'auto': 'jeep',
            'major': 'social sciences',
            'living': 'easy',
            'retire': 65,
            'relocate': 'anywhere',
            'journey': 'just started',
            'sleeptime': 'day time'
            
        }
        
        
        print('\u2588 Starting Our Lesson \u2588', end='\n\n')
        
        test = input('1-tuple, 2-list, 3-dict, 4-exit 5-pass-dict:')
        
        if test.__eq__('tuple'):
            print('\nMain call Object type is: {0}  Memory: {1}'.format(type(a_tuple), id(a_tuple)), end='\n\n')
            packing_tuple(a_tuple)
        
        elif test.__eq__('list'):
            print('Main call tuple Type: {0}  Memory: {1}'.format(type(a_tuple), id(a_tuple)), end='\n\n')
            packing_list(a_list)
            
        elif test == 'dict':
            print('Main call Type: {0}  Memory: {1}'.format(type(a_dict), id(a_dict)), end='\n\n')
            packing_dict(a_dict)
            
        elif test == 'exit':
            print('\u2139 Good Bye \u2139')
            sys.exit(0)
        #print('Main code Does dict abc struct exists Type: {0}  Memory: {1}'.format(type(abc), id(abc)), end='\n\n')
        #packing_args(a_tuple)
        
        elif test.__eq__('pass-dict'):
            ask = input('available:user_dict \tEnter dict: ')
            passing_dict(locals()[ask])
            
        
    except NameError as e:
        print('Exception raised {0}'.format(e))
    
    