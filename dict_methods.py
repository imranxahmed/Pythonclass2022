# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 12:48:13 2022
@author: admin
@Objective: dict and its methods
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
               'business': 'no',
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
    
    ditem = '\t\u2139 dozers \t\n'

    ditem += '\t\u2139 dict_by_keys  \t\n'
    ditem += '\t\u2139 Dict_line -json_dump \t\n'
    ditem += '\t\u2139 pop_dict_item (i) \t\n'
    ditem += '\t\u2139 dict get_item (key) \t\n'   
    ditem += '\t\u2139 dict.clear()  -removes all items from dict\t\n'
    ditem += '\t\u2139 dict_pop_item (key) - not found KeyError is raised\t\n'
    ditem += '\t\u2139 '
    print(ditem, end='\n\n')

def dict_option():
    
    ditem = '\t\u2139 Dict-add \t\n'
    ditem += '\t\u2139 maryam (a) \t\n'
    ditem += '\t\u2139 (h) razina \t\n'
    ditem += '\t\u2139 (i) dozers \t\n'

    print(ditem, end='\n\n')
    
def check_dict(test_dict):
    for item1, item2 in test_dict.items():
        print('{0} set to --> {1}'.format(item1, item2))
    
def iterate_keys(choice):

        if choice == 'dozers':
            for dict_key in dozers.keys():
                print('KEY in dict {0} is: \u2139{1}\u2139\n'.format(choice, dict_key), end='\n')
                print('KEY {0} value: {1} \n'.format(dict_key, dozers[dict_key]), end='\n')
    
        elif choice == 'marym':
            for dict_key in maryam.keys():
                print('KEY in dict {0} is: \u2139{1}\u2139\n'.format(choice, dict_key), end='\n')
                print('KEY {0} value: {1} \n'.format(dict_key, maryam[dict_key]), end='\n')
    
        elif choice == 'hassan_family':
            for dict_key in hassan_family.keys():
                print('KEY in dict {0} is: \u2139{1}\u2139\n'.format(choice, dict_key), end='\n')
                print('KEY {0} value: {1} \n'.format(dict_key, hassan_family[dict_key]), end='\n')
        else:
            print('have NOT selected correct option \n')
            sys.exit(0)
            
def dict_line(dict):
    ''' this fuction also works with nested dicts '''
    print(json.dumps(dict, indent=4))
    
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
      
     '''   
     
if __name__ == "__main__":
    
    print('\t\u2588 We r learning about dict structure \t\u2588', end='\n\n')
    dict_menu()
    
    try:
        
        pick = input('Which dict u want 2 see: ')
        option = input('Select option: ')
        
        iterate_keys(pick)
                    
    except (NameError,TypeError ) as e:
        print('Error: {0}'.format(e))
        
