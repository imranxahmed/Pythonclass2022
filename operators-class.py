# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 08:09:59 2022
Ojbective: Introduction to Operators
@author: Imran Ahmed
"""

import sys

def choices():
    
    menu = '\n\n'
    menu += '\u2139 \t Using Unicode \u2139\n'
    menu += '1:\u2588\tMath Operators: Enter (math) \u2588\n'
    menu += '2:\u2588\tBoolean Operators: Enter (bool) \u2588\n'
    menu += '3:\u2588\tBitwise Operators: Enter (bitwise) \u2588\n'
    menu += '4:\u2588\tRelational Operators: Enter (relation) \u2588\n'
    menu += '5:\u2588\tMembership Operators: Enter (member) \u2588\n'
    menu += '6:\u2588\tIdentity  Operators: Enter (identity) \u2588\n'
    menu += '7:\u2588\tAssignment Operators: Enter (assign) \u2588\n'
    menu += '8:\u2588\tExit program: Enter (exit)'
    menu += '\n\n'
    print(menu)
    
def math_ops():
       
    menu = '\n\n'
    menu += 'Math operators \n'
    menu += 'add : Addition \n'
    menu += 'subtract: Negation \n'
    menu += 'multiply: Multiplication \n'
    menu += 'div: to return a float from division \n'
    menu += 'quotient: to return Integer quotient only from division \n'
    menu += 'modulo: to return remainder from division \n'
    menu += 'divmod: to return both quotient and remainder \n'
    menu += 'power: to return power of num1 raised to power of num2 \n'
    menu += 'tired: To quit this function\n\n'
    print(menu)
    
def relation_ops():
    
    menu = '\n\n'
    menu += 'Relational Operators \n'
    menu += '==:  equal \n'
    menu += '!=:  Not equal \n'
    menu += '<:   Less than \n'
    menu += '>:   greater than \n'
    menu += '<=:  Less than or equal \n'
    menu += '>=:  greater than or equal \n'
    menu += 'Press Ctrl-c exit \n'
    print(menu)
    
def identity_ops():
    
    menu = '\n\n'
    menu += 'Identity Operators'
    menu += 'is: if both operands have same id \n'
    menu += 'is not: if both operands don\'t have same id \n'
    menu += 'When you create an integer object where the value is in range (-5,256) AND \
             string objects greater than or equal to 20 chars, instead \
             of creating different objects at memory for the same value  \
             these objects act as a pointer to already created objects.'
    print(menu)


def membership_ops():
    
    menu = '\n\n'
    menu += 'Membership Operators \n'
    menu += 'in: if a string or sequence is found in string, list or sequence \n'
    menu += 'not in: if a string or seqence is NOT found in a string, list or sequence. \n'
    print(menu)
    
def maths():
    
    while True:
        print('\n\nThese are + - * / // operators', end='\n\n')
        math_ops()
        math_ask = input('Please Enter Operation: ')
        
        if math_ask.__eq__('tired'):
            sys.exit('U r tired of this module. Quitting')
    
        elif math_ask == 'add':
            print('This is addition Math Operators Review', end='\n\n')
            num1 = int(input('Enter First Number: '))
            num2 = int(input('Enter Secnod Number: '))
            print('num1 Type= {0} num2 Type= {1}'.format(type(num1), type(num2)))
            print("The + of {0} and {1} is: {2} ".format(num1, num2, num1 + num2))
            
        
        elif math_ask.__eq__('subtract'):
            
            print('This is subtract Math Operators Review', end='\n\n')
            num1 = int(input('Enter First Number: '))
            num2 = int(input('Enter Secnod Number: '))
            print('num1 Type= {0} num2 Type= {1}'.format(type(num1), type(num2)))
            print("The - of {0} and {1} is: {2} ".format(num1, num2, num1 - num2))
            
        elif math_ask == 'multiply':
            
            print('This is Multiply Math Operators Review', end='\n\n')
            num1 = int(input('Enter First Number: '))
            num2 = int(input('Enter Secnod Number: '))
            print('num1 Type= {0} num2 Type= {1}'.format(type(num1), type(num2)))
            print("The * of {0} and {1} is: {2} ".format(num1, num2, num1 * num2))
            
        elif math_ask == 'div':
            
            '''Divides the number on its left by the number 
            on its right and returns a floating point value.'''
            print('This is float division Math Operators Review', end='\n')
            num1 = float(input('Enter First Number: '))
            num2 = float(input('Enter Secnod Number: '))
            print('num1 Type= {0} num2 Type= {1}'.format(type(num1), type(num2)))
            print("The / of {0} and {1} is: {2} ".format(num1, num2, num1 / num2))
            
        elif math_ask == 'quotient':
            
            '''//: Divides the number on its left by the number on its right, 
            rounds down the answer, and returns a whole number.'''
            print('This is round down division Math Operators Review', end='\n')
            num1 = float(input('Enter First Number: '))
            num2 = float(input('Enter Secnod Number: '))
            print('num1 Type= {0} num2 Type= {1}'.format(type(num1), type(num2)))
            print("The // of {0} and {1} is: {2} ".format(num1, num2, num1 // num2))
            
        elif math_ask == 'modulo':
                
            '''%: Divides the number on its left by the number on its right, 
            and returns the remainder.'''
            print('This is remainder Math Operators Review', end='\n')
            num1 = float(input('Enter First Number: '))
            num2 = float(input('Enter Secnod Number: '))
            print('num1 Type= {0} num2 Type= {1}'.format(type(num1), type(num2)))
            print("The % of {0} and {1} is: {2} ".format(num1, num2, num1 % num2))
            
        elif math_ask == 'divmod':
                
            '''divmod: returns both quotient and remainer.'''
            print('This is divmod Math Operators Review', end='\n')
            num1 = float(input('Enter First Number: '))
            num2 = float(input('Enter Secnod Number: '))
            print('num1 Type= {0} num2 Type= {1}'.format(type(num1), type(num2)))
            print("The divmod of {0} and {1} is: {2} ".format(num1, num2, divmod(num1, num2)))
            
        elif math_ask == 'power':
                
            '''power: returns num1 raised to power of num2.'''
            print('This is power Math Operators Review', end='\n')
            num1 = float(input('Enter First Number: '))
            num2 = float(input('Enter Secnod Number: '))
            print('num1 Type= {0} num2 Type= {1}'.format(type(num1), type(num2)))
            print("The divmod of {0} and {1} is: {2} ".format(num1, num2, num1 ** num2))
            
        else:
            
            return
    

def show_bool():
    
    print("This is Logical or Boolean Operation Module")
    menu = 'Logical Operators are: \n'
    menu += 'AND :Conjunction \n OR "Disjunction \n NOT :Negation\n\n'
    print(menu)
    print('Something is True only when both a AND b are True')
    print('Reference below URL for further reading', end='\n\n')
    print('https://realpython.com/python-and-operator/')
    
    city1 = input('Enter City1 (rutherford): ')
    state1 = input('Enter State1 (nj): ')
    city2 = input('Enter City2 : (philly) ')
    state2 = input('Enter State2 : (ny)')
    
    if city1.__eq__('rutherford') and state1.__eq__('nj'):
        print('Both City1 AND State1 match', end='\n\n')
        print('\t\tIf the first expression evaluated to be false while using \
              and operator, then further expressions are not evaluated.  \
              Also, any string is always considered a true statement.', end='\n\n')
    else:
        print('AND test failed.', end='\n\n')
        
    if city2.__eq__('alabama') or state2.__eq__('delaware'):
        
        print('Either city2 OR state2 matched')
        print("The logical operator OR returns False \
               only if both the operands are False else it returns True. \
               It is a binary operator, which means to return some value, \
               it has to be operated between two operators \
               i.e, two operators are required" )
    
    else:
        
        print('The OR test returned False')
        print('Both OR test failed', end='\n\n')
        
    
    nottest = input('Enter text: ')

    if not nottest.__eq__('world'):
        
        print('True turned to False: {0} '.format(nottest))

    else:
        
        print('False turned to True eqal to: {0}'.format(nottest))
        
def show_bitwise():
    
    print('This function still under work', end='\n\n')
    return

def show_relation():
    
    relation_ops()

    while True:
        try:
            ask_1 = input('Enter item 1: ')
            ask_2 = input('Enter item 2: ')
            
            print('Performing Equality test ==')
            print('is ask_1 {0} == ask_2 {1} : {2}'.format(ask_1, ask_2, ask_1 == ask_2))
            
            print('\nPerforming Not equal test !=')
            print('is ask_1 {0} != ask_2 {1} : {2}'.format(ask_1, ask_2, ask_1 != ask_2))
            
            print('\nPerforming greater than test >')
            print('is ask_1 {0} > ask_2 {1} : {2}'.format(ask_1, ask_2, ask_1 > ask_2))
            
            print('\nPerforming less than test <')
            print('is ask_1 {0} < ask_2 {1} : {2}'.format(ask_1, ask_2, ask_1 < ask_2))
            
            print('\nPerforming greater or  equal test >=')
            print('is ask_1 {0} >= ask_2 {1} : {2}'.format(ask_1, ask_2, ask_1 >= ask_2))
            
            print('\nPerforming less than or equal test <=')
            print('is ask_1 {0} <= ask_2 {1} : {2}'.format(ask_1, ask_2, ask_1 <= ask_2))
            
        except (SyntaxError, KeyboardInterrupt) as err:
            print('\n\tProgram Interrupted')
            print(err)
            
            
def show_member():
    
    membership_ops()
    my_list = []
    
    while True:
        
        names = input('Please add your name (Enter done when finsihed): ')
        
        if names.__eq__('done'):
            print(my_list)
            break
        my_list.append(names)
    
    while True:      
        
        check_name = input('Enter name to check (Type dismiss to exit): ')
        
        
        if check_name.__eq__('dismiss'):
            sys.exit('Exiting show_member')
            
        if check_name in my_list:
            print('Membership test successful')
            print('Student is present.', end='\n\n')
                
        elif check_name not in my_list:
            
            print('Membership test failed')
            print('Student is absent', end='\n\n')
    return    

def show_identity():
    

    id_1 = input('Enter item1: ')
    id_2 = input('enter item2: ')
    
    if id_1 is id_2:
        print('id_1 object {0} is same as id_2 object {1}'.format(id(id_1), id(id_2)))
    else:
        print('id_1 object {0} is NOT as id_2 object {1}'.format(id(id_1), id(id_2)))
    
def show_assign():
    
    print('This function still under work', end='\n\n')
    return
    
    
''' start of Main function '''


def main():
    
    while True:
        
        try:
            choices()
            operation = input('Select Operator to learn:')
            print('U selected {0} Operator:'.format(operation))
            
            if operation.__eq__('exit'):
                print('Exiting.. Thnk U')
                sys.exit()
               
            elif operation.__eq__('math'):
                maths()
            
            elif operation.__eq__('bool'):
                show_bool()
                       
            elif operation.__eq__('bitwise'):
                show_bitwise()
                
            elif operation.__eq__('relation'):
                show_relation()
                
            elif operation.__eq__('member'):
                show_member()
                
            elif operation.__eq__('identity'):
                show_identity()
                
            elif operation.__eq__('assign'):
                show_assign()
                
            else:
                print('Choice Not Found')
                
            
        except KeyboardInterrupt as keyerr:
            print('\n\tProgram Interrupted')
            print(keyerr)
    
''' Main program '''

if __name__ == "__main__":
    
    main()
