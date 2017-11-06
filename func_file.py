from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()

def print_a_line(line, f):
    print line, f.readline()

def rewind(f):
    f.seek(0)

file_name = open(input_file)

print_all(file_name)

rewind(file_name)

c_line = 1
print_a_line(c_line, file_name)

c_line+=1
print_a_line(c_line, file_name)

c_line+=1
print_a_line(c_line, file_name)

print_all(file_name)
