# EXCEPTION HANDLING
'''
- Difference between Errors and Exceptions:
    - Error: syntaxError, invalid syntax when you misspell or mistype the python code (indentation, missing ':' at the end of the line, etc.)
        Error happens during compile time 
    - Exception: even if a statement is syntatically correct, it may cause an error when execution. 
        Errors detected during execution are called exceptions, and are not unconditionally fatal: you can handle them. 
        Exception is an event detected during execution that interrupt the flow of a program.
    
- Exception handling happens in try-except block.
- 'try': enables you to test a code block for errors
- 'except': used to handle exceptions arising in the previous try clause
- 
'''

# EXERCISES:

'''
1. Exercise: IndexError
The below code has one problem. It is trying to locate an item from the list that does not exist. 
Running the code will throw the IndexError. 
Add exception handling to stop the error from being thrown and return a more user-friendly message such as "Item does not exist in the list".

items = [1,2,3,4,5]
item = items[6]
print(item)

'''
items = [1,2,3,4,5]
try:
    item = items[6]
    print(item)
except IndexError as e:
    print('Item does not exist in the list,', e)
    print(e.__class__)


'''
2. Exercise: ZeroDivisionError
In math there are rules about dividing by zero. The below code is trying to do just that and will throw a ZeroDivisionError. 
Add exception handling to return back 0 instead of allowing the error to be thrown.

def divide_by(a, b):
    return a / b

ans = divide_by(40, 0)
print(ans)

'''

def divide_by(a, b):
    try: 
        return a / b
    except ZeroDivisionError:
        return 0
    except Exception as e:
        print('Something went wrong!')


ans = divide_by(40, 0)
print(ans)


'''
3. Exercise: FileNotFoundError
The code below is looking for a file that does not exist. 
Add exception handling to catch this error and return the following "The file could not be found".

with open('file_does_not_exist.txt', 'r') as file:
    print(file.read())

'''

try:
    with open('file_does_not_exist.txt', 'r') as file:
        print(file.read())
except FileNotFoundError as e:
    print(e, 'The file could not be found.')
    print(e.__class__)


'''
4. Exercise: HackerRank - ValueError, ZeroDivisionError
ZeroDivisionError: This error is raised when the second argument of a division or modulo operation is zero.
ValueError: This error is raised when a built-in operation or function receives an argument that has the right type but an inappropriate value.
a = '1', b = '#'
print int(a) / int(b) --> ValueError: invalid literal for int() with base 10: '#'

'''

def calculate_division(a, b):
    try:
        print(int(a) / int(b))
    except ZeroDivisionError as e:
        print("Error Code: ", e)
    except ValueError as e:
        print('Error Code:', e)

calculate_division('3', '0')
calculate_division('3', '$')
calculate_division('9', '3')


'''
5. Exercise: YT video
'''
try:
    num1 = int(input('Enter a number to divide: '))
    num2 = int(input('Enter a number to divide by: '))
    result = num1 / num2
    
except ZeroDivisionError as e:
    print('You can not divide by zero,', e)
except ValueError as e:
    print('Enter only numbers,', e)
except Exception as e:
    print('Something went wrong.', e)

else: 
    print(result)   # we print the result only if there is no exception occurs, and the try block is executed

finally: # it will be always executed, for example to close a file when handling file
    print('This will always execute')


'''
6. Exercise: YT video
'''

# custom exception
# class JustNotCoolError(Exception):
#    pass

my_variable = 3
try:
    #raise JustNotCoolError('I am a custom exception.')

    # print(my_variable / 0)
    
    if not type(my_variable) is str:
        raise TypeError('TypeError. Only strings are allowed.')

except NameError:
    print('NameError means something is undefined.')
except ZeroDivisionError: 
    print('Please do not divide by zero.')
except Exception as e: 
    print(e)
else:
    print("No errors.") # this 'else' block will only execute, if the try block is executed
finally:
    print("I will be always printed no matter what.") # 'finally' will be always executed


