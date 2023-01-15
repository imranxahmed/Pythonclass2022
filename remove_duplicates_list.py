# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 07:02:33 2023

@author: Imran Ahmed
@Objective: remove duplicate items in LIST
"""

    
same = ['next', 'come', 'next', 'come', 'next', 'next', 'built', 'come', 'also']

match = 'next'
count = 0

print('Main list: ', same, end='\n\n')
while count < len(same):
    if same[count].__eq__(match):
        print('index={0} --> Match poped:{1}'.format(count, same.pop(count)))
        count -=1
        print('New index: {0}  --> New len: {1}'.format(count, len(same)))
    else:
        print('skipped index:', count)
        print('List length: {0} \tList: {1}'.format(len(same),same))
        count +=1
        
print('End of duplicate removel. \nFinal list: {0}'.format(same))


# =============================================================================
# dups = ['next', 'come', 'next', 'come', 'next', 'next', 'built', 'come', 'also']
# 
# for index, item in enumerate(dups):
#     if item.__eq__(match):
#         print('poped at Index: {0}'.format(index))
#         dups.pop(index)
#         print('New Length: {0} \tNew List: {1}'.format(len(dups), dups))
#     else:
#         print('skiped Index: {0}'.format(index))
#         
#         
# print('All duplicates removed. \n Final List: ', dups)
# 
# =============================================================================
