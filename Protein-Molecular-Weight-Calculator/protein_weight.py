
amino_acid_weights = {
    'A': 89.09,
    'R': 174.20,
    'N': 132.12,
    'D': 133.10,
    'C': 121.15,
    'Q': 146.15,
    'E': 147.13,
    'G': 75.07,
    'H': 155.16,
    'I': 131.17,
    'L': 131.17,
    'K': 146.19,
    'M': 149.21,
    'F': 165.19,
    'P': 115.13,
    'S': 105.09,
    'T': 119.12,
    'W': 204.23,
    'Y': 181.19,
    'V': 117.15
}

protein = input("Enter Protein Sequence: ").upper()

total_weight = 0

for amino_acid in protein:
    if amino_acid in amino_acid_weights:
        total_weight += amino_acid_weights[amino_acid]
    else:
        print(f"Warning: '{amino_acid}' is not a valid amino acid.")

print("\nProtein Sequence:", protein)
print("Length:", len(protein))
print("Estimated Molecular Weight: {:.2f} Da".format(total_weight))
print("Estimated Molecular Weight: {:.2f} kDa".format(total_weight / 1000))
