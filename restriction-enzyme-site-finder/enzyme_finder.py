from enzymes import restriction_enzymes


def find_sites(sequence):
    sequence = sequence.upper()

    print("\nRestriction Enzyme Analysis")
    print("-" * 35)

    found = False

    for enzyme, site in restriction_enzymes.items():
        positions = []

        start = 0

        while True:
            index = sequence.find(site, start)

            if index == -1:
                break

            positions.append(index + 1)
            start = index + 1

        if positions:
            found = True
            print(f"{enzyme}")
            print(f"Recognition Site : {site}")
            print(f"Positions        : {positions}")
            print()

    if not found:
        print("No restriction enzyme recognition sites found.")


if __name__ == "__main__":
    dna = input("Enter DNA Sequence:\n")
    find_sites(dna)
