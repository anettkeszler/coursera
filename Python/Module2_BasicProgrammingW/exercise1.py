import random

file_name = 'Python/Module2_BasicProgrammingW/petnames.txt'
file = open(file_name, 'r')
file_content = file.read()
file_content_list = file_content.split("\n")
print(random.choice(file_content_list))
file.close()