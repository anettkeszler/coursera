# Algorithms 

# check if a word is a palindrome, palindrome is a word that can be spelled the same both backwards and forwards
# this case, we need to check if the index in front of the string is equal at the end of the string
str = 'racecar'

def is_palindrome(str):
    start_index = 0
    end_index = len(str) - 1

    for x in str:
        if str[start_index] != str[end_index]:
            return False
    return True

print(is_palindrome('racecar'))


# Make a cup of coffee
"""
def make_a_cup_of_coffee():
    list_of_ingredientes = ['coffee']
    sugar = input('do you want sugar? Y or N  ')
    if sugar == 'Y' or 'y':
        list_of_ingredientes.append('sugar')
    
    milk = input('Do you want milk? Y or N ')
    if milk == 'Y' or 'y':
        list_of_ingredientes.append('milk')

    return list_of_ingredientes

print('Your coffee is ready:...')
print(make_a_cup_of_coffee())

"""

# Sorted() function - list is sorted alphabetical order 
coffees = ['Latte', 'Espresso', 'Americano', 'Cappuchino', 'Macchiato']
print(sorted(coffees))

# pure function or not? 
# global scope:
global_list = [1, 2, 3]

def add_to(item):
    return global_list.append(item)

add_to(4)
print(global_list) # [1, 2, 3, 4] --> this is not a pure function as it changes the global_list by appending the item which is passed as an argument 

# create the pure function on the above example 

my_list = [1, 2, 3]

def add_to_pure_function(lst: list, item):
    nl = lst.copy()
    nl.append(item)
    return nl

new_list = add_to_pure_function(my_list, 4)

print(my_list)
print(new_list)


# Reverse a string in Python
# 1. Slicing function - string[start:stop:step]

trial = 'reversal'
new_trial = trial[::-1]

print(new_trial)

# 2. Recursion 
def string_reverse(str: str):
    if len(str) == 0:
        return str
    else:
        return string_reverse(str[1:]) + str[0]

str = 'january'
reverse = string_reverse(str)
print(reverse)

# MAP and FILTER 

menu = ['espresso', 'mocha', 'latte', 'cappuchino', 'cortado', 'americano']

def find_coffee(coffee):
    if coffee[0] == 'c':
        return coffee

# MAP
map_coffee = map(find_coffee, menu)
print(map_coffee)

for x in map_coffee:
    print(x)

# FILTER
filter_coffee = filter(find_coffee, menu)
print(filter_coffee)

for x in filter_coffee:
    print(x)

def summation(n):
   if n == 1:
       return 0
   return n + summation(n-1)

a = summation(5)
print(a)

# LIST COMPREHENSION:
data = [2,3,5,7,11,13,17,19,23,29,31]

# Ex1: List comprehension: updating the same list
data = [x+3 for x in data]
print("Updating the list: ", data)

# Ex2: List comprehension: creating a different list with updated values
new_data = [x*2 for x in data]
print("Creating new list: ", new_data)

# Ex3: With an if-condition: Multiples of four:
fourx = [x for x in data if x%4==0]
print("Divisible by 4: ", fourx)

# Ex4: Alternatively, we can update the list with the if condition as well
fourxsub = [x-1 for x in new_data if x%4 == 0 ]
print("Divisible by four minus one: ", fourxsub)

# Ex5: Using range function:
nines = [x for x in range(100) if x%9 == 0]
print("Nines: ", nines)