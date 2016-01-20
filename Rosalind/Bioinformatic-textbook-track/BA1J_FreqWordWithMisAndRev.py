# BA1J
# Find Frequent Words with Mismatches and Reverse Complements

# Find the most frequent k-mers (with mismatches and reverse complements) in a DNA string.
# Given: A DNA string Text as well as integers k and d.
# Return: All k-mers Pattern maximizing the sum Countd(Text, Pattern) + Countd(Text, Pattern) over all possible k-mers.

from BA1C import ReverseComplement
from BA1G import hamming
from BA1I import Neighbors
from ReadnWrite import *

def FreqWordWithMisAndRev(text, k, d):
	Set = {}
	totalSet = {}
	maxcount = 0
	for i in range(len(text)-k+1):
		pattern = text[i:i+k]
		revpattern = ReverseComplement(pattern)
		if d == 0 :
			newlist = [pattern, revpattern]
		else :
			Neighborpattern = Neighbors(pattern, d)
			revNeighbor = Neighbors(revpattern, d)
			newlist = Neighborpattern + revNeighbor
		for pt in newlist :
			Set[pt] = Set.get(pt, 0) + 1
	for i in Set.keys():
		totalSet[i] = Set[ReverseComplement(i)] + Set[i]
		if maxcount <= totalSet[i] :
			maxcount = totalSet[i]
	for i in totalSet.keys():
		if maxcount == totalSet[i] :
			print i, 
