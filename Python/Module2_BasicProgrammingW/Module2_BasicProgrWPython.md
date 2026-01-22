## Module2: Basic Programming With Python

https://runestone.academy/ns/books/published/pythonds/index.html


Resources:
- More on Python data structures: <br>
https://docs.python.org/3/tutorial/datastructures.html# <br>
https://realpython.com/python-data-structures/ <br>

- Exception handling:<br>
https://docs.python.org/3/library/exceptions.html <br>
https://pynative.com/python/file-handling/ <br>

### Functions
- function is a piece of code that can be re-used repeatedly
- input --> function body --> output
- function can take parameters too

### Variable scoping (LEGB)
- The purpose of scope is to protect the variable 

1. **Local Scope**: 
- refers to a variable that is declared inside a function
- outside of the function will not have access to it
- when you attempt to access the variable outside of the function, Python raises a **NameError** because the variable is out of scope.
- (NameError: name 'total' is not defined)

2. **Enclosing Scope**: 
- refers to a function inside another function or what is commonly called a nested function

3. **Global Scope**: 
- accessible from anywhere in the code 
- when a variable is declared outside of a function

4. **Built-in Scope**: 
- accessible from anywhere in the code
- built-in functions and objects, such as print(), len() (but not the reserved keywords, like def, for, if)
- Built-in scope covers all the language of Python

### Data Structures in Python 
- **Built-in Data Structures**: non-primitive data structures, meaning they are classed as objects
    - List: mutable
    - Tuple: immutable
    - Set
    - Dictionary

- **User-defined Data Structures**:
    - Stack
    - Queue
    - Tree
    - Linked List
    - Graph
    - HashMap

- **Mutability** refers to data inside the data structure that can be modified. For example, you can either change, update, or delete the data when needed. 
- An immutable data structure will not allow modification once the data has been set. 

### LISTS
- Lists are a sequence of one or more different or similar datatypes 
- In Python, it is a dynamic array that can hold any datatype 
- List items can be accessed by its index

- Declaration of a list: 
```
list1 = [] # --> declare an empty list
list1 = [1, 2, 3, 4, 5] # --> List of integers

list2 = ['A', 'B', 'C'] # --> List of strings

list3 = ['A', 1, True, 40.23] # --> List of different datatypes

list4 = [1, [1, 2, 3], 2, 3] # --> Nested list
```

- List functions: 
    - insert(arg1, arg2): expects 2 arguments
        - arg1: the index where the item should be placed
        - arg2: value of the placed item
        - **list.insert(len(list), 6)** --> # it will insert 6 at the end of the list
    
    - append(arg1): expects 1 argument
        - arg1: value of the plced item
        - **list.append(6)** --> # it will append 6 at the end of the list
    
    - extend([list]): expect 1 argument, which can be a list
        - **list.extend([6, 7, 8])** # --> it will extend the list with another list at the end

    - pop(arg1): to remove items from the list
        - arg1: the index of the removable item
        - **list.pop(0)**: it will remove the first item from the list 
    - del list[index]: remove item at the given index
        - del list[2] # --> removes the item on index 2

    
    - Iterate through a list with FOR LOOP

### TUPLES 
- declare an empty tuple:
```
my_tuple = ()
```

- a tuple can accept any mix of data types
```
my_tuple = (4, 'Hello', True, 4.6, 'Hello')
```

- to access the value in tuple is possible by index
```
print(my_tuple[1]) # --> Hello
print(type(my_tuple)) # --> <class 'tuple'>
```

- to get the count of a value, use the count() function:
```
print(my_tuple.count('Hello')) # --> 2, as Hello occures 2 times
```

- get the index of a value
```
print(my_tuple.index(4.5)) # --> 3, the double 4.5 is on index 3
```

- you can iterate through a tuple 
```
for x in my_tuple:
    print(x)
```

- key difference between lists and tuples, that tuples are **immutable**, means that they **can not be changed **
- **Immutability**: Once a tuple is created, its elements cannot be changed. While you can access elements using indexing, you can't modify them or add new ones after creation.

### SETS
- Sets are collections with no duplicates and unordered item 
- Set is not a sequence, so it cannot be indexed. You cannot reach the items by its index (not ordered)
```
my_set1 = {} # --> declare an empty set

my_set1 = {1, 2, 3, 4, 5}
```

- Sets differ from lists in that they don't allow duplicate values 
```
my_set1 = {1, 2, 3, 4, 5, 5} 
print(my_set1) # --> the second 5 is not printed out
```

- Add items to sets
```
my_set1.add(67) # --> 67 will be added at the end of the set
print(my_set1) # --> {1, 2, 3, 4, 5, 67}
```

- Remove items: remove or discard, they does the same
```
my_set1.remove(2) # --> number 2 will be removed
print(my_set1) # --> {1, 3, 4, 5, 67}

my_set1.discard(3) # --> number 3 will be removed
print(my_set1) # --> {1, 4, 5, 67}
```
##### Mathematical operations on sets: 
- **Union** (merges or joins the 2 sets, but exclude the duplicates)
```
my_set1 = {1, 2, 3, 4, 5}
my_set2 = {4, 5, 6, 7, 8}
print(my_set1.union(my_set2)) # --> {1, 2, 3, 4, 5, 6, 7, 8}, it joins the 2 sets but not the duplicate values
print(set_a | set_b)          # --> {1, 2, 3, 4, 5, 6, 7, 8}, same output as the union 
```

- **Intersection**:
```
print(set_a.intersection(set_b)) # --> {4, 5}, we get back the values which occures in both sets
print(set_a & set_b)             # --> {4, 5}, ampersand (&) works the same way as intersection 
```

- **Difference**:
```
print(set_a.difference(set_b)) # --> {1, 2, 3}, it will give back all the elements that are only in set_a, and not in set_b
print(set_a - set_b)           # --> {1, 2, 3}, with minus(-) we get the same output as difference()
```

- **Symmetrical difference**: represents all the elements that are present in set_a or set_b, but not in both sets
```
print(set_a.symmetric_difference(set_b)) # --> {1, 2, 3, 6, 7, 8}
print(set_a ^ set_b) # --> same output with the carrot(^) operator
```

### DICTIONARIES
- Dictionaries access values based on keys (not on index as lists)
- Faster and more flexible as lists: you can go straight to the item you need based on its key
- we assign the key to a specific value --> called **key-value pair**
- Mutable, values can be changed or updated 

- Access the value based on the key:
```
my_dict = {1: 'Coffee', 2: 'Tea', 3: 'Juice'}
print(my_dict[1]) # Coffee
```

- Update the dictionary by replacing an item to another:
```
my_dict[2] = 'Mint Tea' # update the value based on the key
print(my_dict)      # {1: 'Coffee', 2: 'Mint Tea', 3: 'Juice'}
```
- Delete a key-value pair from the dictionary based on the key:
```
del my_dict[3]
print(my_dict)  # {1: 'Coffee', 2: 'Mint Tea'} , delete the key-value pair based on the key
```

- Adding a key-value pair to the dictionary:
```
my_dict[3] = 'Cocoa'
print(my_dict)          # {1: 'Coffee', 2: 'Mint Tea', 3: 'Cocoa'}
```

- If I try to add to put a duplicate key, it doen't allow this, keys must be unique

- Iterate over dictionaries" 

```
for x in my_dict:
    print(x)        # this case only prints the keys 1, 2, 3


for key, value in my_dict.items():
    print(str(key) + " : " + str(value))

Output: 
1 : Coffee
2 : Mint Tea
3 : Cocoa
```

### Args and kwargs(keyword args)
- benefits: you can pass any amounts of **non-keyword variables and keyword arguments**
- ARGS: non-keyword variables
```
def sum_of(a, b):
    print(a + b)

sum_of(4, 5) # 9
# sum_of(4, 5, 6) # TypeError: sum_of() takes 2 positional arguments but 3 were given

sum_of(*args):
    sum = 0
    for x in args:
        sum += x
    return sum

print(sum_of(4, 5, 6)) # 15
```
- Instead of passing 2 arguments, using *args will alow to pass any arguments by calling the function 

- KWARGS: keyword arguments
- let's calculate the total bill in a restaurant
```
sum_of(**kwargs):
    sum = 0
    for key, value in kwargs.items():
        sum += value
    return sum

print(sum_of(coffee=2.99, cake=4.55, juice=2.89))
```

### Exceptions and Errors
1. Syntax Error: 
        - usually caused by the developer (misspelling/type or indentation issues)
        - has minimal impact, because most IDEs warns the developer and gives ideas how to fix them 
2. Exception errors: 
    - they happen during execution 
    - exceptions need to be handled by the developer

### Exception handling
```
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
```
### File handling functions: open() and close()
- Open:
    - open() function is used for reading, writing and creating files 
    - open() function accepts 2 arguments --> open(<file_name>/<file_location>, <mode>)
        - mode indicates the action --> reading, writing, creating
            - 'r' --> open and read in text format
            - 'rb' --> open and read in binary format
            - 'r+' --> open, read and write 
            - 'w' --> open for writing 
            - 'a' --> open for editing or appending 
    
    - close() function: no arguments, it closes the open connection 

    - with open() function: it closes the file automatically 
        



