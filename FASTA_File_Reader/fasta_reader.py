def read_fasta(filename):
    sequences = {}

    with open(filename, "r") as file:
        header = None
        sequence = ""

        for line in file:
            line = line.strip()

            if line.startswith(">"):
                if header:
                    sequences[header] = sequence

                header = line[1:]
                sequence = ""
            else:
                sequence += line.upper()

        if header:
            sequences[header] = sequence

    return sequences


def analyze_sequence(seq):
    length = len(seq)

    a = seq.count("A")
    t = seq.count("T")
    g = seq.count("G")
    c = seq.count("C")

    gc_content = ((g + c) / length) * 100 if length > 0 else 0

    return length, a, t, g, c, gc_content


filename = "sample.fasta"

sequences = read_fasta(filename)

for name, sequence in sequences.items():
    print("=" * 50)
    print("Sequence Name :", name)

    length, a, t, g, c, gc = analyze_sequence(sequence)

    print("Sequence Length :", length)
    print("A :", a)
    print("T :", t)
    print("G :", g)
    print("C :", c)
    print(f"GC Content : {gc:.2f}%")
