# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 12:48:13 2022
@author: admin
@Objective: dict and its methods
"""
import os

test_dict = {
    'name': 'wasil',
    'age': 62,
    'family': 'rathore',
    'weather': 'smoky',  'gender': 'male'}

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

adnan = {
           'father': 'yes',
           'name': 'adnan safee',
           'hobbies': ['rc planes', 'cooking', 'ladoos'],
           'mood': 'happy',
           'eyecolor': 'brown',
           'fav_sports': 'cricket',
           'like_season': 'summers',
           'vacation': 'switzerland'           
    }


anjum = {
           'father': 'no',
           'mother': 'yes',
           'name': 'Anjum chaudhary',
           'hobbies': ['sewing', 'cooking', 'renovation'],
           'mood': 'happy',
           'eyecolor': 'brown',
           'fav_sports': 'basketball',
           'like_season': ['spring', 'summer'],
           'vacation': 'hawaii'           
    }

mirza = {
           'father': 'no',
           'name': 'Mirza Mustafa',
           'hobbies': ['racing', 'coding', 'bunji-jumping', 'hiking'],
           'mood': 'happy',
           'eyecolor': 'brown',
           'fav_sports': 'soccer',
           'like_season': ['spring', 'summer'],
           'vacation': 'Turkey'           
    }

javeed = {
           'father': 'yes',
           'name': 'Javeed Syed',
           'hobbies': ['land scaping', 'coding', 'hiking'],
           'mood': ['happy', 'calm' ],
           'eyecolor': 'black',
           'fav_sports': 'soccer',
           'like_season': ['spring', 'summer'],
           'vacation': 'Turkey'           
    }

maria = {
           'father': 'no',
           'mother': 'yes',
           'name': 'Maria Anjum',
           'hobbies': ['crafting', 'coding', 'bunji-jumping'],
           'mood': 'happy',
           'eyecolor': 'brown',
           'fav_sports': 'soccer',
           'like_season': ['fall', 'summer'],
           'vacation': 'Maldives'           
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
    
    ditem = '\t Menu - Defined dicts\t\n'
    ditem += '\t (a) hassan_family \t\n'
    ditem += '\t (b) adnan \t\n'
    ditem += '\t (c) anjum \t\n'
    ditem += '\t (d) mirza \t\n'
    ditem += '\t (e) javeed \t\n'
    ditem += '\t (f) maria \t\n'
    ditem += '\t (g) maryam \t\n'
    ditem += '\t (h) razina \t\n'
    ditem += '\t (i) dozers \t\n'
    print(ditem, end='\n\n')
    

for item1, item2 in test_dict.items():
    print('{0} set to --> {1}'.format(item1, item2))
    
print('Testing if razina is father or mother')    
if razina['father'].__eq__('no'):

    print('Correct, razina is not a Father \
          \nrazina is a Mother', end='\n\n')


print('\t\u2588 create dict from two list \u2588')
print('\t\u2588 Building my_dict dictionary \u2588')

print('\n\n\tExample #2 test_dict \t', end='\n')
print('\tBuiling dict in dict comprehension format\n')


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

if __name__ == "__main__":
    
    print('\t\u2588 We r learning about dict structure \t\u2588', end='\n\n')
    dict_menu()
    choice = input('Which dict u want 2 see: ')
    
    if choice.__eq__('adnan'):
        for dict_key in adnan.keys():
            print('KEY in dict {0} is: \u2139{1}\u2139\n'.format(choice, dict_key), end='\n')
            print('KEY {0} Attribute: {1} \n'.format(dict_key, adnan[dict_key]), end='\n')
        
    elif choice.__eq__('razina'):
        for dict_key in razina.keys():
            print('KEY in dict {0} is: \u2139{1}\u2139\n'.format(choice, dict_key), end='\n')
            print('KEY {0} Attribute: {1} \n'.format(dict_key, razina[dict_key]), end='\n')
            
    elif choice == 'anjum':
        for dict_key in anjum.keys():
            print('KEY in dict {0} is: \u2139{1}\u2139\n'.format(choice, dict_key), end='\n')
            print('KEY {0} Attribute: {1} \n'.format(dict_key, anjum[dict_key]), end='\n')
    
    elif choice == 'mirza':
        for dict_key in mirza.keys():
            print('KEY in dict {0} is: \u2139{1}\u2139\n'.format(choice, dict_key), end='\n')
            print('KEY {0} Attribute: {1} \n'.format(dict_key, mirza[dict_key]), end='\n')

    elif choice == 'anjum':
        for dict_key in anjum.keys():
            print('KEY in dict {0} is: \u2139{1}\u2139\n'.format(choice, dict_key), end='\n')
            print('KEY {0} Attribute: {1} \n'.format(dict_key, anjum[dict_key]), end='\n')
       
    elif choice == 'dozers':
        for dict_key in dozers.keys():
            print('KEY in dict {0} is: \u2139{1}\u2139\n'.format(choice, dict_key), end='\n')
            print('KEY {0} Attribute: {1} \n'.format(dict_key, dozers[dict_key]), end='\n')

    elif choice == 'marym':
        for dict_key in maryam.keys():
            print('KEY in dict {0} is: \u2139{1}\u2139\n'.format(choice, dict_key), end='\n')
            print('KEY {0} Attribute: {1} \n'.format(dict_key, maryam[dict_key]), end='\n')

    elif choice == 'javeed':
        for dict_key in javeed.keys():
            print('KEY in dict {0} is: \u2139{1}\u2139\n'.format(choice, dict_key), end='\n')
            print('KEY {0} Attribute: {1} \n'.format(dict_key, javeed[dict_key]), end='\n')

    elif choice == 'hassan_family':
        for dict_key in hassan_family.keys():
            print('KEY in dict {0} is: \u2139{1}\u2139\n'.format(choice, dict_key), end='\n')
            print('KEY {0} Attribute: {1} \n'.format(dict_key, hassan_family[dict_key]), end='\n')
    else:
        print('U have not selected correct option \n')
        exit(0)
        

