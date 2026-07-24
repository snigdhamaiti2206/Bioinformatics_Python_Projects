# Codon Frequency Counter

A beginner bioinformatics project written in Python.

## Description

This program reads a DNA sequence from a text file and counts the frequency of every codon (groups of three nucleotides).

Example:

DNA:

ATGGCTGCTAAA

Codons:

ATG
GCT
GCT
AAA

Output:

AAA : 1
ATG : 1
GCT : 2

## Features

- Reads DNA sequence from a file
- Removes spaces and newlines
- Converts lowercase to uppercase
- Counts all codons
- Displays total codons

## Requirements

Python 3.x

No external libraries are needed.

## How to Run

```bash
python codon_counter.py
```

Enter:

```
sample_dna.txt
```

## Example Output

```
Codon Frequency

AAA : 1
ATG : 1
GAT : 1
GCG : 1
GCT : 3
GGC : 1
TAA : 1
TTA : 1

Total Codons: 10
```

## Author

Snigdha Maiti 
