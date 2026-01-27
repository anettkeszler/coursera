# LeetCode practice 

# 9. Palindrome Number 
# Given an integer x, return true if x is a palindrome, and false otherwise.

def is_palindrome(x: int):

    ''' my solution
    int_to_str = str(num)
    start_index = 0
    end_index = len(int_to_str) -1

    for x in str(int_to_str):
        if int_to_str[start_index] != int_to_str[end_index]
            return False
        
        return True 
    '''

    # solution, working for all test cases
    if x < 0 or (x and x % 10 == 0):
        return False
    
    y = 0
    while y < x:
        y = y * 10 + x % 10
        x //= 10
    return x in (y, y // 10)


print(is_palindrome(121))
print(is_palindrome(-121))
print(is_palindrome(10))

