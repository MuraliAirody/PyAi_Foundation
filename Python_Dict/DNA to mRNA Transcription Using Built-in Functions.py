'''In gene expression, messenger RNA (mRNA) is transcribed from a DNA template by replacing each DNA nucleotide with its complementary RNA base:
A → U
T → A
C → G
G → C
Write a program that reads a DNA strand (a string of 'A', 'T', 'C', 'G') from standard input and outputs the corresponding mRNA transcript. Instead of manual loops or dictionary lookups, use your language’s built-in string translation utilities (for example, Python’s str.maketrans and str.translate) to perform the substitution in one call.
Input
A single line containing a non-empty DNA string S (1 ≤ |S| ≤ 10^5), consisting only of the uppercase letters A, T, C, G.
Output
A single line containing the transcribed mRNA string of the same length as S, where each nucleotide has been replaced according to the mapping above.'''

# maketrans translate


dna = "ATCG"
rna = "UAGC"

translation_table = str.maketrans(dna, rna)

dna_input = input().strip()

mrna_output = dna_input.translate(translation_table)

print(mrna_output)