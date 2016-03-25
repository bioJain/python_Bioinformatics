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

def TranslationCode(DNAstring, AAstring):
	TranslationDic = {}
	for i in range(len(AAstring)):
		codon = DNAstring[3*i:3*i+3]
		if codon not in TranslationDic.keys():
			TranslationDic[codon] = AAstring[i]
	return TranslationDic
