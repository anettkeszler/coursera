# FILE HANDLING 

'''
- File handling includes opening, reading and writing files among other operations 
- 2 functions: open() and close()
- Open:
    - open() function is used for reading, writing and creating files 
    - open() function accepts 2 arguments --> open(<file_name>/<file_location>, <mode>)
        - mode indicates the action --> reading, writing, creating
            - 'r' --> open and read in text format
            - 'rb' --> open and read in binary format
            - 'r+' --> open, read and write 
            - 'w' --> open for writing, it will overwrite the existing file 
            - 'a' --> open for editing or appending, it will add the changes at the end of the data 
    
    - close() function: no arguments, it closes the open connection 

    - with open() function: it closes the file automatically 
        
'''


# READING the content of a file 


# declare a variable and assign it to the file location 
# open the file for reading, assign it to a variable 'file'
# read the lines of the file and assign it to a variable 'data'
# close the file
file_name = '/Users/anettkeszler/GitHub/coursera/Python/practice/test.txt'

file = open(file_name, 'r')

data = file.readline()
print(data)
file.close()

# another way to open and read from a file - 'with open() as file' - no need to close the file, it will do automatically
# with open() as file is better at exception handling 

with open(file_name, 'r') as file:
    print(file.readline())


# read(), readline(), readlines()

# read() - returns the entire contents of the file as a string 
    # you can also pass an integer to return only the specified number of characters in the file (read(40)) --> will return the first 40 characters

with open(file_name, 'r') as file:
    print(file.read(3)) # Hel

# readline() function returns a single line as a string 
    # you can pass an integer as argument for returning a specified number of characters on a single line (readline(3)) --> will return the first 3 characters


with open(file_name, 'r') as file:
    print(file.readline(3)) # Hel

# readlines() function reads the entire contents of the file and return it in an ordered list --> you can iterate over the list 
with open(file_name, 'r') as file:
    data = file.readlines()
    print(data)         # list of lines
   
    for line in data:   
       print(line)      # list items is printed out line by line  

# CREATING FILES:
# In Python we can create new files using the open() function and enabling the write mode 

with open('new_file.txt', 'a') as file:
    # file.write('This is a new file I just created!') # for a single line
    file.writelines(['This is the first line', '\nThis is the secong line', '\nThird line', '\nFourth\n']) 
    # if I want to write more lines, writelines() function accepts a list ['first line', 'second line', 'third line']

# every time I run my script in mode 'w', it's replacing the current file  
# if I want to add to my file, I need to change the mode to 'a' - append

try:
    with open('sample/new_file2.txt', 'a') as file:
       file.writelines(['something', 's'])
except FileNotFoundError as e:
    print('File not found', e)
    print(e.__class__)



  
