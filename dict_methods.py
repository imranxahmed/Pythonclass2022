# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 12:48:13 2022
@author: admin
@Objective: dict and its methods
Ref1: https://realpython.com/python-pass-by-reference/
Ref2: https://stackoverflow.com/questions/40796264/what-does-pythons-locals-do
"""
import sys, json

test_dict = {
    
    'name': 'wasil',
    'age': 62,
    'family': 'rathore',
    'weather': 'smoky',  'gender': 'male' 
    
    }

hassan_family = {
    
           'father': { 
               
               'name': 'hassan',
               'age': 33,
               'education': 'Phd',
               'business': 'construction',
               'color': 'black',
               'height': '6ft 1inch'
               },
           
           'mother': {
               
               'name': 'Alia',
               'age': 23,
               'education': 'Phd',
               'business': 'no',
               'color': 'black',
               'height': '6ft'
               },
                
          'child': {
              
              'name': 'mohsin',
              'age': 13,
              'education': 'daycare',
              'business': 'no',
              'color': 'black',
              'height': '3ft 1inch',
              'mood': 'cranky'
              }       
     }


maryam = {
           'father': 'no',
           'mother': 'yes',
           'name': 'Maryam Rahim',
           'hobbies': ['crochet', 'coding', 'scuba-diving', 'hiking'],
           'mood': 'happy',
           'eyecolor': 'brown',
           'fav_sports': 'volleyball',
           'like_season': ['winter', 'summer'],
           'vacation': 'South Korea'           
    }

razina = {
           'father': 'no',
           'mother': 'yes',
           'name': 'Razina shiliwala',
           'hobbies': [ 'coding', 'hiking'],
           'mood': 'happy',
           'eyecolor': 'brown',
           'fav_sports': 'bedminton',
           'like_season': ['spring', 'fall'],
           'vacation': 'Dubai'           
    }

dozers = {
    
    'cat_250': {
        
        'bought': '10-25-2010',
        'model': 'Caterpillar 250 E',
        'hours': '1500',
        'site': 'Florida'
    
        },
    
        
    'cat_300': {
        
        'bought': '1-5-2009',
        'model': 'Caterpillar 300 G',
        'hours': '16000',
        'site': 'Miami'     
        
        }
    
    }

def dict_menu():
    
    ditem = '\t\u2139 a - dict_by_items \t\n'
    ditem += '\t\u2139 b - dict_by_keys  \t\n'
    ditem += '\t\u2139 c - Dict_line -json_dump \t\n'
    ditem += '\t\u2139 d - dict_popitem LIFO \t\n'
    ditem += '\t\u2139 e - dict_get_item (key) \t\n'   
    ditem += '\t\u2139 f - dict_clear()  -removes all items from dict\t\n'
    ditem += '\t\u2139 g - dict_pop_item (key) - not found KeyError is raised\t\n'
    ditem += '\t\u2139 h - dict_search \t\n'
    ditem += '\t\u2139 E - Exit or Quit \t\n'
    print(ditem, end='\n\n')

def dict_option():
    
    ditem = '\n\t\u2139 1 - hassan_family \t\n'
    ditem += '\t\u2139 2 - maryam \t\n'
    ditem += '\t\u2139 3 - razina \t\n'
    ditem += '\t\u2139 4 - dozers \t\n'
    ditem += '\t\u2139 5 - test_dict \t\n'
    ditem += '\t\u2139 6 - options \t\n'
    print(ditem, end='\n\n')
    
def check_dict(choice):

    for item1, item2 in choice.items():
        print('{0} set to --> {1}'.format(item1, item2))
    

def iterate_keys(choice):

        for dict_key in choice.keys():
                print('KEY in dict {0} is: \u2139{1}\u2139\n'.format(choice, dict_key), end='\n')
                print('KEY: {0} value: {1} \n'.format(dict_key, choice[dict_key]), end='\n')
      
def test(**kwargs):
    
    print(id(kwargs))
    print('{key} --> {value}'.format(**kwargs))
    
def dict_line(dicts):
    
    ''' this fuction also works with nested dicts '''
    print(json.dumps(dicts, indent=4))
    
        

def item_pop(choice):
    print('{0} has been popped from {1}.'.format(choice.popitem(), choice))
        
        
def dict_by_item_key(which_dict):
    
        #print(type(which_dict))
        print(which_dict.keys())
        select_key = input('\n\nselect key: ')       
        print('KEY {0} set to: {1}'.format(select_key, which_dict.get(select_key, "Key Not Found")))
        
def clear_a_dict(choice):
    print('dict: {0} is cleared {1}'.format(choice, choice.clear()))
  
def dict_pop_by_key(choice):
    
    try:
        
        print('Keys: {0}'.format(choice.keys()))
        ask_key = input('Select the key to remove: ')
        print('current dict is:\n {0}'.format(choice), end='\n\n')
        print('key: {0} will be removed'.format(ask_key))
        
        #print(choice.pop(ask_key, 'Key Not Found'))
        
    except KeyError as err:
        print('pop failed with msg: {0}'.format(err))
        
        #print('key: {0} from dict: {1} is removed'.format(choice[ask_key]), choice, choice.pop())
    
def dict_search(choice):
    try:
        
    
''' print('\n\n\tExample #2 test_dict \t', end='\n')
    print('\t\u2588Builing dict in dict comprehension format\n') '''


glossary = {
        "mtitle": "example glossary",
            "title": "S",
               "ID": "SGML",
					"SortAs": "SGML",
					"GlossTerm": "Standard Generalized Markup Language",
					"Acronym": "SGML",
					"Abbrev": "ISO 8879:1986",
					"GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
						"GlossSeeAlso": ["GML", "XML"]
                    },
					"GlossSee": "markup"

   }

'''
Method dict.items() 
      It will return both key & value pair
Method is dict.keys()
      It will only return keys
Method is dict.values()
      It will only return values 
      
dict.get(key)   
dict.clear()  -removes all items from dict
dict.pop(key) - not found KeyError is raised
dict.update({'key': 'value'})

In essence, one can say that mutable objects like 
 
         dictionaries, 
         sets, 
         and lists 
         
         are passed by reference. 

Immutable objects like 

      int, 
      str, 
      tuple 
      
      are passed by value.
    
'''   
     
options = { 
    
   
        'dict1': 'hassan_family', 
        'dict2': 'maryam', 
        'dict3': 'razina', 
        'dict4': 'dozers', 
        'dict5': 'test_dict' 
           
           }

if __name__ == "__main__":
    
    print('\t\u2588 Lesson about dict Methods \t\u2588', end='\n\n')
      
    try:
        
        dict_menu()
        pick_method = input('Select function: ')
        
        if pick_method.__eq__('E'):
            sys.exit(0)
        
        dict_option()
        which_dict = input('Select Dict: ')

        if pick_method.__eq__('a'):
            check_dict(locals()[which_dict])
            
            
        elif pick_method == 'b':
            iterate_keys(locals()[which_dict])
        elif pick_method == 'c':
            dict_line(locals()[which_dict])
        elif pick_method == 'd':
            item_pop(locals()[which_dict])
        elif pick_method == 'e':
            dict_by_item_key(locals()[which_dict])    
        elif pick_method.__eq__('f'):
            clear_a_dict(locals()[which_dict])
        elif pick_method.__eq__('g'):
            dict_pop_by_key(locals()[which_dict])
        elif pick_method.__eq__('h'):
            dict_search(locals()[which_dict])
        
            
            
                    
    except (NameError,TypeError ) as e:
        print('Error: {0}'.format(e))
        
