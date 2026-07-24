def detect_mutations(normal, mutated):
    mutations = []

    if len(normal) != len(mutated):
        print("Warning: Sequences have different lengths.")
        min_len = min(len(normal), len(mutated))
    else:
        min_len = len(normal)

    for i in range(min_len):
        if normal[i] != mutated[i]:
            mutations.append(
                {
                    "Position": i + 1,
                    "Original": normal[i],
                    "Mutated": mutated[i]
                }
            )

    return mutations


def main():
    print("=== DNA Mutation Detector ===")

    normal = input("Enter Normal DNA Sequence: ").upper()
    mutated = input("Enter Mutated DNA Sequence: ").upper()

    mutations = detect_mutations(normal, mutated)

    if len(mutations) == 0:
        print("\nNo mutations detected.")
    else:
        print(f"\nTotal Mutations: {len(mutations)}")
        print("-" * 35)

        for mutation in mutations:
            print(
                f"Position {mutation['Position']}: "
                f"{mutation['Original']} → {mutation['Mutated']}"
            )


if __name__ == "__main__":
    main()
