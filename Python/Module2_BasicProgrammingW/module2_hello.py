# Functions 
'''
bill = 175.00
tax_rate = 15

total_tax = (bill * tax_rate) / 100.00
'''


    # define the function 
def calculate_tax(bill, tax_rate):
    return round((bill * tax_rate) / 100, 2)

    # call the function
print(calculate_tax(100, 20))

print(calculate_tax(167, 22))

# Variable scoping

# global scope
my_global = 10

def function1():

    enclosed_variable = 8

    def function2():
        local_variable = 5
        print('Access to global variable', my_global)
        print('Access to enclosed ', enclosed_variable)
        print('Local variable', local_variable)

# print(enclosed_variable) --> not accessed at this scope
# print(local_variable) --> not accessed at this scope

# LISTS

list1 = [1, 2, 3, 4, 5]
print(list1)
print(*list1)
print(list1, sep=" ")

# insert to the list
# insert function expects 2 arguments, the index of where to insert and the value
list1.insert(len(list1), 6) # --> insert 6 to the end of the list
print(list1)

list1.insert(0, 6) # --> insert 6 at the zero index
print(list1)

# append to the list
# append put the value at the end of te list, no need to specify the index where the item should be placed 
list1.append(7)
print(list1)

# extend another list to the list 
# extend will add another list to the end the original list
list1.extend([8, 9, 10])
print(list1)

# remove items from the list:
# pop(index)
list1.pop(0) #--> remove the first item from the list, at index zero
print(list1)

list1.pop(len(list1)-1) # --> remove the last item from the list
print(list1)

# del keyword
del list1[0] # --> deletes the first itrem in the list, at zero index
print(list1)

# TUPLES

my_tuple = ()
my_tuple = (1, 'Hello', True, 4.5, 'Hello')

print(type(my_tuple))
print(my_tuple)

# count the occurances of an item
print(my_tuple.count('Hello')) # --> 2, as Hello occures 2 times

# get the index of a value
print(my_tuple.index(4.5)) # --> 3, the double 4.5 is on index 3

# iterate through a loop
for x in my_tuple:
    print(x)


# SETS
my_set = {1, 2, 3, 4, 5, 5}
print(my_set) # --> {1, 2, 3, 4, 5}, they don't allow duplicate values

# adding to the set
my_set.add(67) # --> it will be added at the end of the set
print(my_set)

# remove item from the set
my_set.remove(2) # --> number 2 will be removed
print(my_set) # --> {1, 3, 4, 5, 67}

# merges or join 2 sets
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print(set_a.union(set_b)) # --> {1, 2, 3, 4, 5, 6, 7, 8}, merges the 2 sets but not the duplicate values

print(set_a | set_b)      # --> {1, 2, 3, 4, 5, 6, 7, 8}, same output as the union()

# intersection 
print(set_a.intersection(set_b)) # --> {4, 5}, we get back the values which occures in both sets
print(set_a & set_b)             # --> {4, 5}, ampersand (&) works the same way as intersection() 

# difference
print(set_a.difference(set_b)) # --> {1, 2, 3}, it will give back all the elements that are only in set_a, and not in set_b
print(set_a - set_b)           # --> {1, 2, 3}, with - we get the same output as difference()

# Symmetrical difference
print(set_a.symmetric_difference(set_b)) # --> {1, 2, 3, 6, 7, 8}, we get back all of the elements that are present in set_a or set_b, but not in both sets
print(set_a ^ set_b)    # {1, 2, 3, 6, 7, 8}

# DICTIONARIES

# access the value based on the key
my_dict = {1: 'Coffee', 2: 'Tea', 3: 'Juice'}
print(my_dict[1]) # Coffee

# update the dictionary by replacing an item to another
my_dict[2] = 'Mint Tea' # update the value based on the key
print(my_dict)      # {1: 'Coffee', 2: 'Mint Tea', 3: 'Juice'}

del my_dict[3]
print(my_dict)  # {1: 'Coffee', 2: 'Mint Tea'} , delete the key-value pair based on the key

# adding a key-value pair to the dictionary
my_dict[3] = 'Cocoa'
print(my_dict)       # {1: 'Coffee', 2: 'Mint Tea', 3: 'Cocoa'}   

# Iterate over dictionaries

for x in my_dict:
    print(x)        # this case only prints the keys 1, 2, 3


for key, value in my_dict.items():
    print(str(key) + " : " + str(value))

my_set = {1, 2, 3, 2, 4}
my_set.add(5)
my_set.add(3)
print(my_set)

# ARGS and KWARGS 

# args
def sum_of(a, b):
    print(a + b)

sum_of(4, 5) # 9
# sum_of(4, 5, 6) # TypeError: sum_of() takes 2 positional arguments but 3 were given

def sum_of(*args):
    sum = 0
    for x in args:
        sum += x
    return sum
print(sum_of(4, 5, 6))  # 15
print(sum_of(4, 5, 6, 7, 8, 9)) # 39

# kwargs
def sum_of(**kwargs):
    sum = 0
    for key, value in kwargs.items():
        sum += value
    return round(sum, 2)

print(sum_of(coffee=2.99, cake=4.99, juice=3.89)) 

# Exception handling
def divide_by(a, b):
    return a / b

print(divide_by(40, 4)) # 10
# print(divide_by(40, 0)) # ZeroDivisionError: division by zero
# To handle this, use try-except block

try:
    ans = divide_by(40, 0)
except Exception as e:
    print("Something went wrong!", e) # prints out the message and the type of the message (e)
    print(e.__class__) # it prints out the type or class of the exception (<class 'ZeroDivisionError'>)

# you can add more except block
try:
    divide_by(40, 0)
except ZeroDivisionError as e: 
    print(e, 'We can not divide by zero')
except Exception as e:
    print('Something went wrong', e)


try:
    with open('file_does_not_exist.txt', 'r') as file:
        print(file.read())
except FileNotFoundError as e:
    print(e, "file doesn't exist")
    print(e.__class__)

# File handling
# open and read from a file, than close the file
file = open('Python/Module2_BasicProgrammingW/test.txt', 'r')
data = file.readline()
print(data)
file.close()

# with open --> closes the file automatically

with open('Python/Module2_BasicProgrammingW/test.txt', 'r') as file:
    data = file.readline()
    print(data)

# Creating a file: file.write("")
with open('Python/Module2_BasicProgrammingW/new_file.txt', 'w') as file:
    file.write('This is a new file created!') # a new file is created with the given text

# Creating a file with multiple lines:
# file.writelines("") --> accepts a list 
try: 
    with open('Python/Module2_BasicProgrammingW/new_file_w_multiple_line.txt', 'a') as file:
        file.writelines(['\nThis is the first line!', '\nThis is the second line!', '\nThird line'])
except FileNotFoundError as e:
    print(e, "File not exists.")


# Reading files: 
with open('Python/Module2_BasicProgrammingW/new_file_w_multiple_lines.txt', 'r') as file:
    file.read()
