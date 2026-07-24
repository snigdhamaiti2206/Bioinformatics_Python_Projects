def reverse_complement(dna_sequence):
    """
    Generates the reverse complement of a DNA sequence.
    """
  
    complement = {
        "A": "T",
        "T": "A",
        "G": "C",
        "C": "G"
    }

    dna_sequence = dna_sequence.upper()

    for base in dna_sequence:
        if base not in complement:
            return "Error: DNA sequence contains invalid nucleotide(s)."

    reversed_sequence = dna_sequence[::-1]

    reverse_complement_sequence = ""

    for base in reversed_sequence:
        reverse_complement_sequence += complement[base]

    return reverse_complement_sequence

print("=" * 40)
print("      Reverse Complement Generator")
print("=" * 40)

dna = input("Enter DNA Sequence: ")

result = reverse_complement(dna)

print("\nOriginal Sequence : ", dna.upper())
print("Reverse Complement:", result)
