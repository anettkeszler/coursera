import random 

# read a file with pet names, each name in a separate line, and return a list of strings with the pet names
def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.readlines()

# Choose a random petname from the given list and return it 
def choose_random_petname(petname_list):
    return random.choice(petname_list)

def main():
    print("hello")

    file_name = '/Users/anettkeszler/GitHub/coursera/Python/practice/petnames.txt'

    file_contents = read_file(file_name)
    print(file_contents)

    print(choose_random_petname(file_contents))


if __name__ == "__main__":
    main()