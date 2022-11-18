List comprehension
Easier and more readable way to create a list

nums = [1,2,3,4,5,6,7,8,9,10]
leters = [abc,life,stem,verb,temp,cool,world]

Example 1

# I want 'n' for each 'n' in nums
#my_list = [ n for  n in nums]
print my_list

my_list = []
for n in nums:
     my_list.append(n)
print my_list 

+++++
Example 2

#I want 'n*n' for each 'n' in nums

#my_list = [ n*n for  n in nums ]
print my_list

my_list = []
for n in nums:
  my_list.append(n*n)
print my_list 

++++

Example 3

#using a map + lambda. Lambda is anonymous function
#map is a function that creates a list
my_list = map(lambda n: n*n, nums)
print my_list 

++++

Example 4

#I want 'n' for each 'n' in nums if 'n' is even
#my_list = [ n for n in nums if n%2 == 0 ]
#print my_list

my_list = [ n for n in nums if 
my_list = []
for n in nums:
  if n%2 == 0:
      my_list.append(n)
print my_list

++++

Example 5
#using filter + Lambda
#filter will only give us values that EVEN
my_list = filter(lambda n: n%2 == 0, nums)
print my_list

Excercise: get ODD values with list comprehension

++++
Example 5
#I want a (letter, num) pair for each letter in 'abcd' and each number in '0123'
my_list = []
for letter in 'abcd':
   for num in rangex(4):
        my_list.append((letter, num))
print my_list

list comprehension
my_list = [ (let, num) for let in 'abcd' for num in xrange(4) ]
print my_list

++++

Example 6
names = ['bruce', 'clark', 'peter', 'logan', 'wade' ]
heros = [ 'batman', 'superman', 'spiderman', 'wolverine', 'deadpool' ]

print zip(names, heros)

dictionary comprehension

I want a dict{'name': 'hero' } for each name,hero in zip(names, heros)
my_dict = {}
for name, hero in zip(names, heros):
    my_dict[name] = hero
print my_dict

my_dict = { name: hero for name, hero in zip(names, heros) if name != 'Peter'}
print my_dict

++++++++
set comprehension ; its a list of unique values

nums = [1,2,3,4,5,6,7,8,9,10,11,11,12,14,13]

my_set = set()
for n in nums:
    my_set.add(n)
print my_set

set comprehension - U can add conditionals at the end of comprehension
my_set = { n for n in nums }
rpint my_set


generator expressions

#I want to yield 'n*n' for each 'n' in nums

def gen_func(nums):
   for n in nums:
         yeild n*n

my_gen = gen_func(nums)

for i in my_gen:
    print i

#generator comprehension
my_gen = (n*n for n in nums)

for i in my_gen: 
    print i
