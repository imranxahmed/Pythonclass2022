# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 07:48:42 2022

@author: Imran Ahmed
Objective: generators

"""
''' How generators work 

    square generator 

   Take a value and create a generator object.
   once a generator object has been called, it can't be used again,
   Unless U define generator object AGAIN

'''

try:
    square = (x*x for x in range(10))
    num1  = [n for n in range(10), m for m in range(10, 50)] 
    
    
    ''' This iteration will produce output '''
    print('\t\u2139 1st iteration of generator Object has output \n\n')
    for num in square:
        print('Square: {0}'.format(num), end='\n\n')
    

    ''' 2nd iteration will not have output '''


    print('What is generator "square" object set to? \
          after calling the generator {0}'.format(square))

    print('\t\u2139 2nd iteration has NO output')
    for num in square:
        print('square {0}:'.format(num), end='\n\n')

except NameError as e:
        print('NameError raised {0}: '.format(e))
    