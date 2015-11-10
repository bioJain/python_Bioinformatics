# BA1B
# Find the Most Frequent Words in a String

import BA1A

def FrequentWord(text, k):
	frequentPT = {}
	maxcount = 0
	for i in range(len(text)-k+1):		
		temp_pattern = text[i:i+k]
		if not temp_pattern in frequentPT.keys():
			temp_count = BA1A.patternCount(text, temp_pattern)
			frequentPT[temp_pattern] = temp_count
			if temp_count >= maxcount :
				maxcount = temp_count
	for key in frequentPT.keys():
		if frequentPT[key] == maxcount:
			print key, 
