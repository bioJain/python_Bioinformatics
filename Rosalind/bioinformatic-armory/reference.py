# Bioinformatic Armory

# INI : Introduction to the Bioinformatics Armory
# Given: A DNA string s of length at most 1000 bp.
# Return: Four integers (separated by spaces) representing the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s. Note: You must provide your answer in the format shown in the sample output below.

def CountNT(string):
	count = [0]*4
	nt = ['A', 'C', 'G', 'T']
	for number in range(len(nt)):
		count[number] = string.count(nt[number])
	return count


# DBPR : Introduction to Protein Databases
# Given: The UniProt ID of a protein.
# Return: A list of biological processes in which the protein is involved (biological processes are found in a subsection of the protein's "Gene Ontology" (GO) section).

# manually found ; better get used to using Biopython


# MEME : New Motif Discovery
# Given: A set of protein strings in FASTA format that share some motif with minimum length 20.
# Return: Regular expression for the best-scoring motif.


# PTRA : Protein Translation
# Given: A DNA string ss of length at most 10 kbp, and a protein string translated by s.
# Return: The index of the genetic code variant that was used for translation. (If multiple solutions exist, you may return any one.)

from Bio.Seq import translate

def CheckCodeTable(DNAstring, AAstring):
	for i in range(1, 16):
		if translate(DNAstring, table=i, stop_symbol="") == AAstring:
			return i


# RVCO : Complementing a Strand of DNA
# Given: A collection of nn (n =< 10) DNA strings.
# Return: The number of given strings that match their reverse complements.

from ReadnWrite import *

def CheckComplement(DNAlist):
	DNAdic = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
	count = 0
	for item in DNAlist:
		DNAcompl =''
		for nt in item[::-1] :
			DNAcompl += DNAdic[nt]
		if DNAcompl == item :
			count += 1
	return count


# OPFR : Finding Genes with ORFs

# reference : codon table

CodonTable = {'UUU':'F', 'CUU':'L', 'AUU':'I', 'GUU':'V', 'UUC':'F', 'CUC':'L', 'AUC':'I', 'GUC':'V', 'UUA':'L', 'CUA':'L', 'AUA':'I', 'GUA':'V', 'UUG':'L', 'CUG':'L', 'AUG':'M', 'GUG':'V', 'UCU':'S', 'CCU':'P', 'ACU':'T', 'GCU':'A', 'UCC':'S', 'CCC':'P', 'ACC':'T', 'GCC':'A', 'UCA':'S', 'CCA':'P', 'ACA':'T', 'GCA':'A', 'UCG':'S', 'CCG':'P', 'ACG':'T', 'GCG':'A', 'UAU':'Y', 'CAU':'H', 'AAU':'N', 'GAU':'D', 'UAC':'Y', 'CAC':'H', 'AAC':'N', 'GAC':'D', 'UAA':'Stop', 'CAA':'Q', 'AAA':'K', 'GAA':'E', 'UAG':'Stop', 'CAG':'Q', 'AAG': 'K', 'GAG':'E', 'UGU':'C', 'CGU':'R', 'AGU':'S', 'GGU':'G', 'UGC':'C', 'CGC':'R', 'AGC':'S', 'GGC':'G', 'UGA':'Stop', 'CGA':'R', 'AGA':'R', 'GGA':'G', 'UGG':'W', 'CGG':'R', 'AGG':'R', 'GGG':'G' }

def ORFfinder(DNAstring):
	DNAstring = DNAstring.replace('T', 'U')	
	ORFdic = {}	
	i = 0
	while i <= len(DNAstring):
		j = DNAstring.find('AUG', i)
		if j == -1:
			break
		else:
			newDNA = DNAstring[j:]
			AAstring = ''
			for k in range(int(len(newDNA)/3)):
				codon = newDNA[3*k:3*k+3]
				if CodonTable[codon] == 'Stop':
					ORFdic[len(AAstring)] = AAstring
					i = j + 1
					break
				elif k == int(len(newDNA)/3)-1:
					ORFdic[len(AAstring)] = AAstring
					i = j + 1
					break
				else :
					AAstring += CodonTable[codon]
	maxvalue = max(ORFdic.keys())
	print(maxvalue)
	return ORFdic[maxvalue]

def ReverseTranslate(DNAstring):
	DNAdic = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
	newDNA = ''
	for nt in DNAstring[::-1]:
		newDNA += DNAdic[nt]
	return newDNA
