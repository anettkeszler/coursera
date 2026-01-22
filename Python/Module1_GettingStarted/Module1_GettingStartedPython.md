# Programming with Python

## Module1: Getting Started with Python 

Source: https://www.coursera.org/learn/programming-in-python/lecture/3vpix/introduction-to-the-course

Python website: https://docs.python.org/3/library/functions.html

To practice: https://www.hackerrank.com/domains/python

w3School coding and learning: https://www.w3schools.com/python/default.asp


### What is programming? 
Programming is a set of instructions in a language the computer understands, to perform a specific operation, task or function. 

### Python
- one of the most popular programming languages to learn 
- has lots of frameworks and libraries
- widely used in all areas of business (web developement, AI, machine learning, data analytics, applications)
- easy to learn and get started with
- require less code in comparison to Java, so it makes developers very productive and allows projects to be completed more quickly 
- "write less, do more" philosophy

### Installing Python paths (on Mac)
By default, an Apple Mac has Python installed with version 2.7. You can verify this by opening up a terminal and running the following command: 
```
python --version
```
- You need to install a few dependencies before installing python:
    - XCode: command-line tool to handle homebrew
    - Homebrew or 'brew': package manager for Mac 
```
brew install python
```

When you install python via brew, it will install version 3.x.
To verify that you have both versions installed run the following:
```
python --version  
python3 --version 
```

### Environment check for Mac in VSCode
- create a .py file
- set up the python interpreter: search for 'python: select interpreter', choose the one it's recommended or which comes with the most recent version 

### Running python code - command line vs IDE (VSC)
1. Running code in Python shell: 
    - useful for running and testing small scripts
    - no need to create a .py file
    - you just add your code that can run directly in the shell 

- if you type 'python' in the Python shell, it opens a shell where you can run python code
- type 'exit()' to exit the Python shell

2. Running a Python file from the command line or Terminal 
```
python(3) hello.py
```
It is better to run Python in VSC compared to running it in the Python shell or in the command line, because VS Code features include auto-completion, code syntax, highlighting and debugging, whitespace and indentation helpers. 

### Python syntaxm, spaces, functions
```
print("Hello"); print("world")
```
- semicolon(;) separates them into 2 lines 

- any amount of whitespace on a single line: no impact when running the code
```
x = 1 +     3
```
- backslash(```\```) at the end of the line: will continue to run the next line 
- Any amount of whitespace or indentations on a line is fine, but keep in mind that if you are combining it with additional lines, then you will need to give 
clear indicators of where a new line has occurred. (```\```)

##### Functions: 
allow you to group code into reusable blocks
```
def function_name(parameters):
    function body
    return result


def say_hello():
    print('Hello there!')

print(say_hello())


def say_hello(): print('Hello there!')

print(say_hello())
```
##### Comments: 
There are multiple reasons why you need to add comments to a code file:
    - Explaining what the code is intended to do
    - Let developers know that code is deprecated
    - Add TODO comments for work to be completed at a later time

- Single-line comments: ```# I'm a single line comment```

- Multi-line comments: triple single or double quotes (``` OR """)

- Inline comments: ```x = 1 # resetting size```

### Variables
- Variables stores different types of data  
- To create variable you need to declare a name and assign it a value  
- To change the value of a variable that has already been declared, you only need to reassign or redeclare it 
- Naming conventions:
    - camelCase: first letter is lowercase, and the first letter of every world after is uppercase with no space between words (myFirstName) 
    - snake_case: everything is lowercase, but use an underscore between words (my_first_name)

- When creating a variable, python automatically assigns the datatype for you
```
x = 5 (integer)
y = 'Hello' (string)
```
- You can declare multiple variables and assignt them to a single value:
``` 
a = b = c = 10
```
- You can declare multiple variables and assign them to multiple values: 
```
a, b, c = 1, 2, 3
```
- You can delete a variable:
```
del x
```

### Basic Data types 
- Numeric: 
    - **Integer**: 
        - integer class (class 'int') represents any non-fractional number
        - whole numbers with no decimal points
        - can be positive or negative (10, -10)
    - **Float**: 
        - contains decimal places (2.9)
        - represented by the floats class (class 'float') 
    - **Complex Number**: 
        - represents the complex class
        - contains both real and imaginary numbers (a = 10 + 10j)
- Sequence: 
    - **String**: 
        - sequence of characters that is enclosed in a single or double quotes
        - represented by the string class (class 'str')
    - **List**: 
        - sequence of one or more different or similar types
        - they are an array and hold any type inside square brackets
        - (class 'list')
        - example_list = [10, 'hello', 24.2]
        - each items can be accessed by its index
    - **Tuples**: 
        - contain an ordered sequence of one or more types
        - but they are immatable: the values cannot be modified or changed 
        - represented by the tuple class (class 'tuple')
- **Dictionary**: 
    - stores data in a key-value objects
    - each value can be accessed directly by its key
    - can store any data type
    - ed = {'a': 23, 'b':44.3}
    - ed['a'] --> 23
- **Boolean**: 
    - true or false
    - type(False) / type(True) --> class 'bool'
- **Set**: 
    - unordered an non-indexed collection of non-repeated values 
    - example_set = {1, 'hello', 4.5, "A"}
    - type(example_set) --> class 'set'

- to determine a type of a variable, use type() function, which provides the class type 
- when you declare a variable in Python, the datatype is automatically assigned based on the value

### Strings
- String is a sequence or collection of characters enclosed in quotes (single or double) 
- if your string is too long for one line, you can add a backslash (```\```) at the end of each line to create a multi line declaration
- strings are much like an array, you can access individual characters based on an index 
- each character in the sequence can be accessed based on its index 
- length of the string: len() function
- concatenation: joining of separate strings
```
name = 'Anett'
print(name[2]) # --> e
print(len(name)) # --> 5

a = 'Hello'
b = 'World!'
print(a + ' ' + b)
```

- str() function: it converts the provided vale into String:
```
str(55)     # outcome: '55'
```

- int() function: convert the provided value into an int:
```
int('75')   # outcome: 75
```
- float() function: can be used to convert the provided value into a float
```
some_int = 10
float(some_int)     # outcome: 10.0
```

### Type casting (aka. data type conversion)
- typecasting is the process of converting one data type to another 
- implicit data type conversion: is automatically by Python's compiler to prevent data loss (int --> float). It only works if the data types are compatible (int - float).
- explicit data type conversion: when implicit conversion throws a type error
    - int('55') --> 55
    - str(45) --> '45'
    - float('20.45') --> 20.45
    - ord() --> returns an integer representing the underlying unicode character 
    - hex() --> converts a given integer to a hexadecimal string 
    - oct() --> takes an integer and returns a string representing an oct to a number  

### User input, console output 
- input() function is designed to get data from the user
```
email = input('Please enter your email address: ')
print(email)
```

#### Print function:
- used for outputs in Python 
- used to print all different types of data, and allows for more complex formatting 
- accepts any number of arguments
```
print(1, 2, 3)              # comma separated arguments
print(1 + 3)                # aritmetic 
name = 'John'
print('Hello ' + name)      #string concatenation
```
- print() function also have keywords that can be passed as additional arguments 
    - object()
    - sep() --> defines how objects being printed or separated 
    - end() --> defines what gets printed at the end
    - file() --> specifies where values get printed to (by default it is STD out)
    - flush() --> boolean expression to flush the buffer, which moves the data to a temporary storage 

### Math and logical operation 
- Operations in Python can be:
    - Mathematical
    - Logical
    - Comparison 

- **Mathematical operations**: 
    - addition: +
    - subtraction: -
    - division: /
    - multiplication: *

- **Logical operators**: <br>
They used in **conditional statements** to determine a True or False outcome.
    - and: checks for all conditions to be true 
    - or: checks for at least one conditions to be true 
    - not: return false if the result is true 


### Control flow: if, else, else if (elif)
- Control flow refers to the order in which the instructions in a program are executed 
- **Control flows can be**:
    - **Conditional** (statements): if, else, else if (elif)
    - **Loops**: for loop, while loop 

```
# Light switch example - Light is currently off (False)
current = False

if current:
    current = False
    print('Turning light off')
else: 
    current = True
    print('Turning light on')
```
- if statement will check if the light is on and if it is, the flow will go inside the condition and set the current variable to False - turning the light off. In the above code snippet, the value of the current variable is initially set to False, so this condition is not met.

- The second if statement will check if the light is off and if it is, the flow will go inside the condition and will set the current variable to True - turning the light on. 

### Match statement 
- use match statement when you test a variable against many conditions 
- compares a value to several different conditions until one of these conditions is met 
- this is an alternative of the if statement 
- when its a lot of statements, it gets messy --> with match statements you can achieve cleaner, more readable code  

### Loops
- Looping is used to iterate through the sequence and access each item inside the sequence 
- FOR LOOP:  
```
str = 'Looping'
fot char in str:
    print(char)
```
- in a standard for loop, I don't have access to the index, but I can use the enumerate function to do that:
```
favorites = ['Banana', 'Apple', 'Tiramisu', 'Cake']

for idx, item in enumerate(favorites):
    print(idx, item)
```

- WHILE LOOP:
- need the set up a condition, than a counter and set the count to 0
- the loop will run while the count is less than the length of the list 
- I have to increment the count by 1 at the end of the block, if not, it will end up in an infinite loop (keep looping until the compiler stops it from running out of memory)
```
while count < len(favorites):
    print("My favorite food is: ", favorites[count])
    count +=1
```

### Controlling flow and loops (break, continue, pass)

- In many cases, you may need to search for a particular item in a list. Once the item is found, there is no need to continue looping over the other results. 
```
favorites = ['Banana', 'Apple', 'Tiramisu', 'Cake']
for dessert in favorites:
    if dessert == 'Tiramisu':
        print('Yes, one of my favorite desserts is ', dessert)
```
- But what happens if you look for a dessert and that dessert is not on the list? The code above is currently not set up to handle this. Let's look for the dessert "Pudding" which is not on the list, and also add an else statement to handle the case of when it's not found. If the dessert is not part of the list, you will print a new statement.

```
favorites = ['Banana', 'Apple', 'Tiramisu', 'Cake']
for dessert in favorites:
    if dessert == 'Tiramisu':
        print('Yes, one of my favorite desserts is ', dessert)
        break
    else:
        print('No sorry, that dessert is not on my list')
```
```
favorites = ['Banana', 'Apple', 'Tiramisu', 'Cake']
for dessert in favorites:
    if dessert == 'Pudding':
        print('Yes, one of my favorite desserts is ', dessert)
else:
    print('No sorry, that dessert is not on my list')
```
- The else will execute only once after the entire for loop is checked and if the dessert we want is not in the list. The else statement is used here in conjunction with the for loop, and so called the **for-else**. 

- **Continue**: Similar to break, continue can be used to control the iteration of the loop. The key difference is that it can allow you to skip over a section of the loop but then continue on with the rest. If you change your code to this, you will notice the outcome will print everything except the Churros dessert.
```
favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

for dessert in favorites:
    if dessert == 'Churros':
        continue
    print('Other desserts I like are', dessert) 

```

- **Pass**: The pass statement in this case acts as a placeholder, allowing you to include an empty block of code without causing a syntax error. It does nothing and allows the program to continue execution normally.
```
for dessert in favorites:
    if dessert == 'Churros':
        pass
    print('Other desserts I like are', dessert) 
```

### Nested Loops
- use to solve complex problems 
```
# outer loop
for x in range(10):
    print(x)
    # inner loop
    for y in range(10):
        print(y)
```