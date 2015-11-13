# BA1G
# Compute the Hamming Distance Between Two Strings

# Compute the Hamming distance between two DNA strings.
# Given: Two DNA strings.
# Return: An integer value representing the Hamming distance.

def hamming(s1, s2):
	hd = 0
	for i in range(len(s1)):
		if s1[i] != s2[i] :
			hd += 1
	return hd
