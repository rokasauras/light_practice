def DNA_strand(dna):
    # Dictionary mapping each DNA base to its complementary base.
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

    # Generate the complementary DNA strand by iterating over each base in the input dna string,
    # using the complement dictionary to find the corresponding complementary base,
    # and joining these bases together into a new string.
    complementary_strand = ''.join(complement[base] for base in dna)

    # Return the resulting complementary DNA strand.
    return complementary_strand

# Example usage:
print(DNA_strand("ATCG"))  # Output: "TAGC"
