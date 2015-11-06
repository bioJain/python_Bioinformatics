# extract all the numbers in the file and compute the sum of the numbers

import re

# first 'f' object is example
# f = open('regex_sum_42.txt')

f = open('regex_sum_166855.txt')
data = ''
for line in f.readlines() :
	data += line

digitlist = re.findall('[0-9]+', data)

total = 0
for digit in digitlist :
	if digit.isdigit() :
		total += int(digit)
print total
