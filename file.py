from sys import argv

script, file_name  = argv

txt = open(file_name,'r+')

print txt.read()

print "Please input three lines to add to the file!"

line1 = raw_input(">")

line2 = raw_input(">")

line3 = raw_input(">")

txt.write(line1)
txt.write("\n")
txt.write(line2)
txt.write("\n")
txt.write(line3)
txt.write("\n")

print txt.read()

txt.close()

