# Introduction - easy

'''
2. Python If-Else
Given an integer perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range 2 of 5 to , print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20 , print Not Weird

Expected Output:
n = 3 --> Weird
n = 24 --> Not Weird
'''

n = 3

if n % 2 != 0 or ((n % 2 == 0) and (n >= 6 and n <= 20)):
    print("Weird")
elif ((n % 2 == 0) and (n >= 2 and n <= 6)) or ((n % 2 == 0) and (n > 20)):
    print("Not weird")

'''
3. Print the 
The included code stub will read an integer,n , from STDIN.
Without using any string methods, try to print the following:
123...n
Note that "..." represents the consecutive values in between.
Example:
n=5
Print the string 12345.
Constraints: 1<=n<=150
'''

n = int(input())

result = []
for i in range(n):
    result.append("{}".format(i+1))

print("".join(result))

'''
4. Python: Division
The provided code stub reads two integers, a and b, from STDIN.
Add logic to print two lines. The first line should contain the result of integer division, a //b . The second line should contain the result of float division, a /b .
No rounding or formatting is necessary.
Example: a = 3, b = 5
The result of the integer division: 3//5=0
The result of the float division is: 3/5=0.6
'''
a = int(input())
b = int(input())

print(a//b)
print(a/b)
