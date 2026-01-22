""" 
Exercise 1: Reads and returns the entire contents of a file as a single string.
    [IMPLEMENT ME]
        1. Open and read the given file into a variable using the File read()
           function.
        2. Print the contents of the file.
        3. Return the contents of the file.

    Args:
        file_name (str): Name of the file to be read.

    Returns:
        str: Entire contents of the file.
"""

def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.read()



"""
Exercise 2: Reads a file and returns a list where each element is a line in the file.
    [IMPLEMENT ME]
        1. Open the given file.
        2. Read the file line-by-line and append each line to a list.
        3. Return the list.

    Args:
        file_name (str): Name of the file to be read.

    Returns:
        list: List where each item is a line from the file.
"""
def read_file_into_list(file_name):
    with open(file_name, 'r') as file:
        return file.readlines()



"""
Exercise 3: Writes the first line of a given string to an output file.
    [IMPLEMENT ME]
        1. Get the first line of file_contents.
        2. Use the File write() function to write the first line into a file
           with the name from output_filename.

        The first line is everything in a string before the first newline ('\n') character.

    Args:
        file_contents (str): String containing multiple lines of text.
        output_filename (str): Name of the file to write the first line into.
"""

def write_first_line_to_file(file_contents: str, output_file_name):
    # print(file_contents.split('\n')[0])
    
    with open(output_file_name, 'w') as file:
        print(file.write(file_contents.split('\n')[0])) 
   


"""
Exercise 4: Reads even-numbered lines of a file and returns them as a list.
    [IMPLEMENT ME]
        1. Open and read the given file into a variable.
        2. Read the file line-by-line and add the even-numbered lines to a list.
        3. Return the list.
    Args:
        file_name (str): Name of the file to be read.
    Returns:
        list: List of even-numbered lines in the file (2, 4, 6, etc.).
"""
def read_even_numbered_lines(file_name):
    i = 1
    list_of_even_numbered_lines = []
    with open(file_name, 'r') as file:
        for line in file.readlines():
            if i % 2 == 0:
                list_of_even_numbered_lines.append(line)
            i += 1
    return list_of_even_numbered_lines


"""
Exercise 5: Reads a file and returns a list of its lines in reverse order.
    [IMPLEMENT ME]
        1. Open and read the given file into a variable.
        2. Read the file line-by-line and store the lines in a list in reverse order.
        3. Print the list.
        4. Return the list.
    Args:
        file_name (str): Name of the file to be read.
    Returns:
        list: List of lines from the file in reverse order.
"""
def read_file_in_reverse_order(file_name):
    list_of_lines_in_reverse_order = []

    with open(file_name, 'r') as file:
        for line in file.readlines():
            list_of_lines_in_reverse_order.append(line)

    return list_of_lines_in_reverse_order[::-1]

def main():

    file_name = 'Python/practice/sampletext.txt'

    print("Exercise 1:")
    file_contents = read_file(file_name)
    print(file_contents)
    print(type(file_contents))

    print("Exercise 2:")
    print(read_file_into_list(file_name))
    print(type(read_file_into_list(file_name)))

    print("Exercise 3:")
    print(write_first_line_to_file(file_contents, 'output.txt'))

    print("Exercise 4:")
    print(read_even_numbered_lines(file_name))\
    
    print("Exercise 5:")
    print(read_file_in_reverse_order(file_name))



if __name__ == "__main__":
    main()
    
