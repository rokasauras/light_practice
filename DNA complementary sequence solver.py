def DNA_strand(dna):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

    complementary_strand = ''.join(complement[base] for base in dna)

    return complementary_strand



