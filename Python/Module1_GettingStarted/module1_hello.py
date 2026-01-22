'''
print('hello')

# semicolon separates them into 2 lines
print('Hello'); print('world')

# whitespace or indentation: no impact when running code
x = 1 +       3
print(x)

# backslash at the end will include the next line 
# Output is 12 
y = 1 + 4 \
 + 7
print(y)

# Data types of variables - type() function 
a = 10
print(type(a))

b = 12.1
print(type(b))

c = 10 + 10j
print(type(c))

d = {'a': 23, 'b':44.3}
print(type(d))

e = 'hello Anett'
print(type(e))

f = [1, 2, 3, 4, 5]
print(type(f))

# Strings - indexing
name = 'Anett'
print(name[2]) # --> e
print(len(name))


a = 'Hello'
b = 'World!'
print(a + ' ' + b)

print("Where do you live?")
location = input()
print("So you live in " + location)

def say_hello(name):
    return "Hello " + name

print(say_hello("Anett"))

# input() function
name = input('Please enter your name: ')
print(name)
print(type(name))

num1 = input('Please enter the first number: ') # 5
print(num1)
print(type(num1))

num2 = input('Please enter the second number: ') #4
print(num2)

print(num1, num2)
print(num1+num2) # 54 - both are strings

# t do calculation, convert them into integers (explicit data type conversion)
print(int(num1)+int(num2))

# concatenation
str1 = input('Please enter your first name: ')
str2 = input('Please enter your second name: ')
print('Hello ' + str1 + ' ' + str2)

print('Hello {} {}'.format(str1, str2))

# Exercise1
age = int(input('What is your age? '))
print(f"Type of age variable is: {type(age)}. It should be <class 'int'>")

height = float(input('What is your height in meters? '))
print(f"Type of height variable is: {type(height)}. It should be <class 'float'>")

loyalty = bool(input('Are you part of our loyalty program? '))
print(f"Type of loyalty variable is: {type(loyalty)}. It should be <class 'bool'>")

# Exercise2
coffee = float(input('1 coffee @: $ '))
sandwich = float(input('1 sandwich @: $ '))
cake = float(input('1 cake @: $ '))

bill_total = coffee + sandwich + cake
print('Your total bill is $', bill_total)

# Logical operators
a = True
b = True

if a and b:
    print("All true!")
'''
    

# Conditional statements: 
from re import match


bill_total = 210

discount1 = 10
discount2 = 20 

if bill_total > 100 and bill_total < 200:
    print("Bill is greater than 100.")
    bill_total = bill_total - discount1
elif bill_total > 200:
    print("Bill is greater than 200.")
    bill_total = bill_total - discount2
else:
    print("Bill is less than 100.")

print("Total bill:  " + str(bill_total))

# my example:
age = 2
ticket_price = 100

if age < 3: 
    print("Age is less than 3, entering is free.")
    ticket_price = 0
elif age > 3 and age < 9:
    print("Age is between 3 and 9, 50 percent discount for the tickets")
    ticket_price = ticket_price * 0.50
else:
    print("Ticket price for adults.")
    ticket_price

print("Ticket price is: " + str(ticket_price))


#Light is currently off
current = False

if current:
    current = False
    print('Turning light off')
else: 
    current = True
    print('Turning light on')

# another example 
loyalty_customer = False
total_bill = 130

if loyalty_customer and total_bill > 100:
    # give 20%
    total_bill = total_bill - (total_bill * 0.20)
elif total_bill > 100:
    # give 10% 
    total_bill = total_bill - (total_bill * 0.10)
else:
    print("Sorry, no discount")

print(total_bill)

# match statement
http_status = 501

match http_status:
    case 200 | 201:
        print('Success')
    case 400:
        print('Bad Request')
    case 500 | 501:
        print('Server Rrror')
    case _:
        print("Unknown")

# For Loop
str = 'Looping'

for char in str:
    print(char)

for i in range(4):
    print('Looping..', i)


favorites = ['Banana', 'Apple', 'Tiramisu', 'Cake']

for item in favorites:
    print('My favorite food is:', item)

for idx, item in enumerate(favorites):
    print(idx+1, item)

# While loop 
count = 0

while count < len(favorites):
    print("My favorite food is: ", favorites[count])
    count +=1

# control flows
favorites = ['Banana', 'Apple', 'Tiramisu', 'Cake']

for dessert in favorites:
    if dessert == 'Tiramisu':
        print('Yes, one of my favorite dessert is ', dessert)
        break
else:
    print('No sorry, that dessert is not on my list')

for dessert in favorites:
    if dessert == 'Tiramisu':
        continue
    print('Other desserts I like are', dessert) 

# nested for loop
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

count2 = 0

# outer loop
for x in list1:     # --> runs 9 times
    count2 += 1
    # inner loop    # --> runs 9 * 9 = 81 times
    for y in list2:
        count2 += 1

print(count2) # 90

# Exercise
num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]

# 1. Under the num_list create a new for loop and print out each value on the list in sequential order.
for num in num_list:
    print(num)
    

# 2.  Inside the for loop, create a condition that will look for all numbers that are greater than 45 and print out only numbers that meet that condition
print('2. *****')
for num in num_list:
    if num > 45:
        print(num)
    else:
        continue   


# 3.  Change the print statement to “Over 45” and add an else condition with a print statement of “Under 45”.
print('3. *****')
for num in num_list:
    if num > 45:
        print("Over 45")
    else:
        print("Under 45")


# 4.  Update the for loop to use the enumerate function so you can get and use the index. 
# Alter the condition to look for number 36 and print out the following: ‘Number found at position: ‘, index number
print('4. *****')
for idx, num in enumerate(num_list):
    if num == 36:
        print('Number found at position', idx)


# 5.  Next, create a new variable called count and assign it a value of 0 and place it outside the for loop.
# 6.  Inside the for loop increment the counter by 1.
# 7.  Add a print statement outside the for loop to print the value of the count variable.
# 8.  Finally, add a break statement directly after the print statement inside the if condition for finding the number. 

counter = 0

for idx, num in enumerate(num_list):
    counter+=1
    if num == 36:
        print('Number found at position', idx)
        break
print(counter)

