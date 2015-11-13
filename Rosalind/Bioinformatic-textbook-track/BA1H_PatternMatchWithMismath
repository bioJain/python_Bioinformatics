# BA1H
# Find All Approximate Occurrences of a Pattern in a String

# Find all approximate occurrences of a pattern in a string.
# Given: Strings Pattern and Text along with an integer d.
# Return: All starting positions where Pattern appears as a substring of Text with at most d mismatches.

# to calculate the hamming distance between two strings
from BA1G import hamming
from ReadnWrite import *

def PatternMatchWithMis(pattern, text, d):
	startingIndex = []
	for i in range(len(text)-len(pattern)+1):
		pattern2 = text[i:i+len(pattern)]
		if hamming(pattern, pattern2) <= d:
			startingIndex.append(i)
	return startingIndex

'''
# compute the given problem
givenData = readExcFirstnLast('rosalind_ba1h.txt')
Ans = PatternMatchWithMis('TGTCCAGCCTGA', givenData, 5)
for i in Ans :
	print i, 
'''
