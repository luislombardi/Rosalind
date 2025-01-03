<<<<<<< HEAD
<<<<<<< HEAD
""" Problem
A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.

An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

Given: A DNA string s
 of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s
.
"""

s = open("C:\\Users\\Usuario\\Downloads\\rosalind_dna.txt").read()

a = s.count("A")
c = s.count("C")
g = s.count("G")
t = s.count("T")

=======
s = open("C:\\Users\\Usuario\\Downloads\\rosalind_dna.txt").read()

a = s.count("A")
c = s.count("C")
g = s.count("G")
t = s.count("T")

>>>>>>> 31750ee3c41068074e22e8f7d4a45727f92c21f8
print(a, c, g, t)
=======
'''
Problem
A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.

An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

Given: A DNA string s
 of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s
'''


s = open("C:\\Users\\Usuario\\Downloads\\rosalind_dna.txt").read()

a = s.count("A")
c = s.count("C")
g = s.count("G")
t = s.count("T")

print(a, c, g, t)
>>>>>>> fb0208494fd4b8e71d31be6223ad4b48f00a68b3
