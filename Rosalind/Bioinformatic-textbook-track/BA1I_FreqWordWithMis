# BA1I
# Find the Most Frequent Words with Mismatches in a String

# Find the most frequent k-mers with mismatches in a string.
# Given: A string Text as well as integers k and d.
# Return: All most frequent k-mers with up to d mismatches in Text.

# to calculate the hamming distance between two strings
from BA1G import hamming
from ReadnWrite import *

def FreqWordWithMis(text, k, d):
	Set = {}
	maxcount = 0
	for i in range(len(text)-k+1):
		pattern = text[i:i+k]
		Neighborpattern = Neighbors(pattern, d)
		for pt in Neighborpattern :
			Set[pt] = Set.get(pt, 0) + 1
			if Set[pt] >= maxcount :
				maxcount = Set[pt]
	for i in Set.keys():
		if maxcount == Set[i] :
			print i,

def Neighbors(pattern, d):
	if d == 0:
		return pattern
	if len(pattern) == 1:
		return ['A', 'C', 'G', 'T']
	Neighborhood = []
	SuffixNeighbors = Neighbors(pattern[1:], d)
	for text in SuffixNeighbors :
		if hamming(pattern[1:], text) < d :
			for nt in ['A', 'C', 'G', 'T']:
				Neighborhood.append(nt+text)
		else :
			Neighborhood.append(pattern[0]+text)
	return Neighborhood

#print FreqWordWithMis('CACAGTAGGCGCCGGCACACACAGCCCCGGGCCCCGGGCCGCCCCGGGCCGGCGGCCGCCGGCGCCGGCACACCGGCACAGCCGTACCGGCACAGTAGTACCGGCCGGCCGGCACACCGGCACACCGGGTACACACCGGGGCGCACACACAGGCGGGCGCCGGGCCCCGGGCCGTACCGGGCCGCCGGCGGCCCACAGGCGCCGGCACAGTACCGGCACACACAGTAGCCCACACACAGGCGGGCGGTAGCCGGCGCACACACACACAGTAGGCGCACAGCCGCCCACACACACCGGCCGGCCGGCACAGGCGGGCGGGCGCACACACACCGGCACAGTAGTAGGCGGCCGGCGCACAGCC', 10, 2)

#Data = readExcLast('rosalind_ba1i.txt')
#FreqWordWithMis(Data, 7, 2)
