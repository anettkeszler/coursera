# Module 3: Programming Paradigms 

- A programming paradigm is an approach to solve the problem using some programming language or also we can say it is a method to solve a problem using tools and techniques that are available to us following some approach. 
- All programming languages need to follow some strategy when they are implemented and this methodology/strategy is paradigms.
- Apart from varieties of programming languages, there are lots of paradigms to fulfill each and every demand.
- Python supports three types of **Programming paradigms**:
    - **Procedural programming paradigms** (imperetive)
    - **Object Oriented programming** (imperetive)
    - **Functional programming** (declarative)

- DRY - Don't Repeat Yourself  
- the main purpose of a programming model is to structure your code.
- You will likely use a combined approach that relies on procedural, object oriented and functional programming paradigms 

### Procedural Programming
- it's like writing a step-by-step instructions that program executes 

- PP structures code into procedures / subroutines 

pros: <br>
    - easy to learn <br>
    - reusable <br>
    - easy to understand <br>
cons: <br>
    - hard to maintain and extend <br>
    - doesn't relate well to real world objects <br>
    - data is exposed throughout the whole program <br>

### Algorithms 
- an algorithms is a series of steps to complete a given task or solve a problem 


### Make a cup of coffee

Step 1: Start with the inputs - what is needed to make a cup of instant coffee?
water, coffee, sugar 

Step 2: Think about all the steps required in the physical aspect of making a cup of instant coffee.
mug, spoon, microwave 

Step 3: Consider the edge cases of optional things like milk or sugar, some people may want it. 
alternative milk, no sugar, no milk

Step 4: The algorithm when complete should have as its final result a cup of coffee.

Tips: Planning is key with any algorithm. Make sure you have all the steps neatly laid out. 

### Algorithmic complexity, efficiency, BigO Notation 
- the code is measured by time and complexity 
- **time**: how long it takes to run the code
- **space**: how much memory it uses 
- **BigO Notation** has different categories ranging from horrible to excellent, and **used to measure the algorithm's efficiency in terms of time and space** 

- **Big O notation** is a fundamental concept in computer science and programming that helps you analyze and describe the efficiency of algorithms. It provides a standardized way of expressing how the runtime or resource usage of an algorithm grows as the size of the input data increases.

- Big O notation is written as "O(f(n))," where "f(n)" is a function that represents the relationship between the input size (usually denoted as "n") and the algorithm's runtime or resource usage.

- Big O notation is a mathematical notation that describes the upper bound or worst-case scenario for the time complexity of an algorithm. It helps us answer questions like:
    - How does the runtime of an algorithm change as the input data gets larger?
    - How does an algorithm scale with increased input size?

    - **Constant time - O(1)** :  
        - same time and space regardless of the size, 
        - the runtime does not depend on the size of the input data
        - it remains constant, making it the **most efficient scenario**.
        - Example:
            - dictionary: to get the value of an item you need to have the key
                - the key is a direct pointer to the value and does not require any iteration to find 
            - Accessing an element in an array by its index

    - **Linear time - O(n)**: 
        - this will grow depending on the size of the input 
        - array of integers with a range of 100, it will very fast. But if it increased to 1 million, it take a lot longer to complete 
        - Example: 
             - Searching for a specific value in an unsorted list
    - **Logaritmic time - O(log n)**: 
        - the runtime grow logarithmically with the size of the input data
        - Logarithmic time complexity is considered very efficient
        - binary search: it splitting the list into 2 parts , and each time to check if a target is less than or greater than one. 
    
    - **Quadratic time - O (n^2)**: 
        -  the runtime grow with the square of the input size
        - Example: 
            - nested list
            - Bubble Sort

    - **Exponencial time - O(2^n)**:
        - this occurs in algorithms where for each increase in the size of the data set, the runtime is doubled. 
        - fibonacci 

    - **Factorial runtime - O(n!)**:
        - terrible runtime 
        - Any algorithm that performs permutation on a given data set is an example of O(n!)

**A Quick Breakdown**:
- Fastest: **Constant time** - **O(1)** Lightning-fast! - accessing a value based on its key in a dictionary 
- Pretty Fast: **O(log n**) - **Logarithmic Time**: Still quite speedy! It grows slowly as you add more data. - binary search 
- Moderate: **O(n)** - **Linear Time:** Respectable speed! If you have twice as much data, it takes about twice as long. It's like looking through a list of names one by one to find a match.
- Slower: **O(n log n)** - **Linearithmic Time**: It's faster than quadratic but slower than linear. An example of O(n log n) time complexity is the Merge Sort algorithm, which divides an array into smaller parts, sorts them, and then merges them back together.
- Slower Still: **O(n^2)** - **Quadratic Time**: Getting slower as you add data. Like checking every combination of items on a list against each other – not great for large lists.
- Quite Slow: **O(2^n)** - **Exponential Time**: Now we're talking about slow! It grows rapidly as you add data. Imagine a puzzle where you have to try every possible combination – it's really slow even for small puzzles.
- Incredibly Slow: **O(n!)** - **Factorial Time**: The slowest of all! It's like solving a complex puzzle where the number of possible arrangements explodes as you add more pieces. Practically unusable for large problems. An example of O(n!) time complexity is generating all possible arrangements (permutations) of a list of items, like finding all possible seating arrangements for a group of people.


Source: https://dev.to/sarah_chima/the-big-o-notation-an-introduction-34f7

### Different types of algorithms in Data structure 
- An Algorithm is a sequence of steps that describe how a problem can be solved.
- The Algorithm are different Categories which are described as below:
    1. Search − Algorithm to search an item in a data structure.
    2. Sort − Algorithm to sort items in a certain order.
    3. Insert − Algorithm to insert item in a data structure.
    4. Update − Algorithm to update an existing item in a data structure.
    5. Delete − Algorithm to delete an existing item from a data structure.

    These are the categories by which every problem become easy and can easily solved.

- **Types of Algorithm**:
    1. **Recursive Algorithm**: it’s an algorithm that calls itself repeatedly until the problem is solved.

    2. **Divide and Conquer Algorithm**: divide the algorithm into two parts, the first parts divides the problem on hand into smaller subproblems of the same type. Then on the second part, these smaller problems are solved and then added together (combined) to produce the final solution of the problem.
    e.c: Merge sort, Quick sort

    3. **Dynamic Programming Algorithm**: these algorithms work by remembering the results of the past run and using them to find new results.
    e.c: Fibonacci sequence
    ```
    Fib(n)
        if n=0
            return 0
        else
            prev_Fib=0,curr_Fib=1
        repeat n-1 times  /*if n=0 it will skip*/
            next_Fib=prev_Fib+curr_Fib   
            prev_Fib=curr_Fib
            curr_Fib=new_Fib
        return curr_Fib
    ```
    4. **Greedy Algorithm**: <br>
    This one finds the best solution in each and every step instead of approaching optimization in a global way.

        A greedy algorithm builds up a solution piece by piece, always choosing the option that looks best at the current step. It makes locally optimal choices in the hope that they lead to a globally optimal solution. Greedy algorithms are simple and efficient, but they only work correctly when the problem has the greedy-choice property (a global optimum can be reached by choosing local optima) and optimal substructure. Examples include activity selection, Huffman coding, Kruskal’s and Prim’s algorithms for minimum spanning trees, and Dijkstra’s algorithm for shortest paths.  

    5. **Brute Force Algorithm**:
    This is one of the simplest algorithms in the concept. A brute force algorithm blindly iterates all possible solutions to search one or more than one solution that may solve a function. Think of brute force as using all possible combinations of numbers to open a safe.
    Example: Exact string, Matching algorithm

    6. **Backtracking Algorithm**: 
    It solves a subproblem and if it fails to solve the problem, it undoes the last step and starts again to find the solution to the problem.
    Example: Queens problem is one good example to see Backtracking algorithm in action. The N Queen Problem states that there are N pieces of Queens in a chess board and we have to arrange them so that no queen can attack any other queen in the board once organized.


### Functional programming: 
- it is processing large amounts of data at hight speed 
- clean, consistent, maintainable code 
- does not change the data outside the scope of the function --> the function should avoid modifying the input data or arguments being passed, instead it should only return the completed result of the intended function being called 
- functions are considered standalone or independent
- example: sorted() function--> it sorts the list in alphabetical order, and logic behind is built-in 
- functions are reusable and that saves a lot of developemtn time 


### Pure functions 
- Pure functions vs traditional functions 
- how to use pure functions in functional programming 

A pure function is used in functional programming because it does not change or have any effect on a variable, data, list, or set beyond its own scope.         
        example: if you have a list with a global scope , a pure function can not add something to that list 

- Benefits: 
    - You always know what outcome will be 
    - Consistent and reliable snippets of the code, that do exactly what they are intended to do 
    - They can be cached since you know the return is always going to be the same 
    - Good options in nulti-threaded program, where more than one process can run concurrently 

### Recursion: 
- is a function that calls itself 
- creates a pattern of repeating itdelf over and over 
- always consider the result , if you don't, it will spin into an infinite loop and suck up all the memory until the program eventually crashes or gets terminated  

### Reversing a string - Python
- some languanges have a built-in function to reverse a string, but Python doesn't
- there are 2 ways to reverese a string in Python:
    1. Slice function: 
     string[start:stop:step] - extended slice syntax
        - start and stop parameters are the indices between which the function manipulates the string 
    
    2. Recursion: 
    https://realpython.com/python-recursion/

### Map and filter 

- map() and filter() function accept 2 arguments 
    - 1sr argument: the function that I use to mach values based on condition 
    - 2nd argument: is the list that I will passe through the function 

- different between map() and filter(): 
    - map() takes all objects in a list and applies a function 
    - filter() do the same, but take the results and creates a new list with only the true values 


### Source: 
Functional Programming: 
https://stackabuse.com/functional-programming-in-python/

List Comprehension:
https://www.upgrad.com/blog/python-list-comprehension/

### Comprehensions: 
- Comprehensions in Python are a way to create a new sequence from an already existing sequence.
    - List comprehension 
    - Dictionary comprehension 
    - Set comprehension 
    - Generator comprehension

1. List Comprehension: 
```
[<expression> for x in <sequence> if <condition>]
```
See examples in .py file. 

- The given example provides different ways in which the list comprehensions can be used to update the list or generate a new list. Comprehensions provide a short-hand and elegant way of updating sequences. As may be evident, the same code can be written using the conventional for loop and if else conditions.

- For instance, in the case of example 1:
```
# List comprehension:
data = [x+3 for x in data]

# Regular for loop:
for x in range(len(data)):
    data[x] = data[x] + 3
```