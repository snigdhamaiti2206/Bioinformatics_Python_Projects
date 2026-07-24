def analyze_dna(sequence):
    sequence = sequence.upper()

    valid = {"A", "T", "G", "C"}

    if not set(sequence).issubset(valid):
        print("Invalid DNA Sequence!")
        return

    print("DNA Sequence:", sequence)
    print("Length:", len(sequence))
    print("A:", sequence.count("A"))
    print("T:", sequence.count("T"))
    print("G:", sequence.count("G"))
    print("C:", sequence.count("C"))

    gc = (sequence.count("G") + sequence.count("C")) / len(sequence) * 100
    print(f"GC Content: {gc:.2f}%")

dna = input("Enter DNA Sequence: ")
analyze_dna(dna)
