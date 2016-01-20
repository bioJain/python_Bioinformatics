# BA1K
# Generate the frequency array of a DNA string.

# Given: A DNA string Text and an integer k.
# Return: The frequency array of k-mers in Text.

from BA1L import PatternToNumber
from ReadnWrite import *

def FreqArray(Text, k) :
	Freq = [0] * 4**k
	for i in range(len(Text)-k+1) :
		pattern = Text[i:i+k]
		index = PatternToNumber(pattern)
		Freq[index] += 1
	return Freq
