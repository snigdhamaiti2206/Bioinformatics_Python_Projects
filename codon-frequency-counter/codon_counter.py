from collections import Counter

def clean_sequence(sequence):
    """Remove spaces/newlines and convert to uppercase."""
    sequence = sequence.replace("\n", "").replace(" ", "").upper()
    return sequence

def count_codons(sequence):
    codons = []

    # Read sequence in groups of 3
    for i in range(0, len(sequence) - 2, 3):
        codon = sequence[i:i+3]
        if len(codon) == 3:
            codons.append(codon)

    return Counter(codons)

def main():
    filename = input("Enter DNA file name: ")

    with open(filename, "r") as file:
        dna = file.read()

    dna = clean_sequence(dna)

    codon_counts = count_codons(dna)

    print("\nCodon Frequency:\n")
    print("--------------------------")

    for codon, count in sorted(codon_counts.items()):
        print(f"{codon} : {count}")

    print("--------------------------")
    print(f"Total Codons: {sum(codon_counts.values())}")

if __name__ == "__main__":
    main()
