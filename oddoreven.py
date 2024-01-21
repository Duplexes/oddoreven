import os
import re

num = int(input('Enter a number: '))
def add_if_statement(num):
    with open('oddoreven.py', 'r') as f:
        lines = f.readlines()
    with open('oddoreven.py', 'w') as f:
        for line in lines[:25]:
            f.write(line)
    for i in range(1, num + 1):
        with open('oddoreven.py', 'a') as f:
            if i == 1:
                f.write('\nif num == 1:\n')
                f.write('\tprint("1 is odd")\n')
            else:
                f.write('elif num == ' + str(i) + ':\n')
                if i % 2 == 0:
                    f.write('\tprint("' + str(i) + ' is even")\n')
                else:
                    f.write('\tprint("' + str(i) + ' is odd")\n')
    with open('oddoreven.py', 'a') as f:
       f.write('\nelse:\n')
       f.write('\tadd_if_statement(num)\n')
       f.write("\tos.system('python oddoreven.py')\n")

if num == 1:
	print("1 is odd")
elif num == 2:
	print("2 is even")
elif num == 3:
	print("3 is odd")
elif num == 4:
	print("4 is even")
elif num == 5:
	print("5 is odd")
else:
	add_if_statement(num)
	os.system('python oddoreven.py')
