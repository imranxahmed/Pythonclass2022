# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 20:11:13 2022

@author: Imran Ahmed
Topic: Dictionary Data structure

"""

# The concept is to represent any informatino with a key value pair


names = ['bruce', 'clark', 'peter', 'logan', 'wade', 'bruce' ]
heros = [ 'batman', 'superman', 'spiderman', 'wolverine', 'deadpool', 'screetch' ]

#print(zip(names, heros))

'''dictionary comprehension

based on concept of KEY,VALUE. we are free to choose key and the value
the elements of dict are NOT ordered.
'''

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
    
    ditem = '\t Menu \t\n'
    ditem += '\t We have below dicts defined \t\n'
    ditem += '\t hassan_family \t\n'
    ditem += '\t adnan \t\n'
    ditem += '\t anjum \t\n'
    ditem += '\t mirza \t\n'
    ditem += '\t javeed \t\n'
    ditem += '\t maria \t\n'
    ditem += '\t maryam \t\n'
    ditem += '\t razina \t\n'
    ditem += '\t dozers \t\n'
    print(ditem)
    
    
if razina['father'].__eq__('no'):
    print('No this is NOT possible', end='\n\n')

#I want a dict{'name': 'hero' } for each name,hero in zip(names, heros)

print('\t\u2588 create dict from two list \u2588')
print('\t\u2588 Building my_dict dictionary \u2588')

my_dict = {}

for k,v  in zip(names, heros):
    
    my_dict[k] = v
    print( my_dict)

#my_dict = { name: hero for name, hero in zip(names, heros) if name != 'Peter'}
#print my_dict

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
    
    
    