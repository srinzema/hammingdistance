#!/usr/bin/env python3
import argparse
from typing import List
from itertools import combinations


def hamming_distance(seq1: str, seq2: str) -> int:
    """Calculate the Hamming distance between two sequences."""
    return sum(n1 != n2 for n1, n2 in zip(seq1, seq2))


def max_hamming_distance(sequences: List[str]) -> int:
    """Calculate the maximum Hamming distance among a list of sequences."""
    return max(hamming_distance(a, b) for a, b in combinations(sequences, 2))


def main() -> None:
    """Parse command line arguments and output the max Hamming distance."""
    parser = argparse.ArgumentParser(
        description="Output max Hamming distance among sequences as integer"
    )
    parser.add_argument("-s", "--sequences", nargs="+",
                        help="List of sequences separated by spaces")
    parser.add_argument("-f", "--file",
                        help="Path to file with one sequence per line")
    args = parser.parse_args()

    if not args.sequences and not args.file:
        parser.error("Provide either --sequences or --file")

    if args.sequences:
        seqs = args.sequences
    else:
        with open(args.file) as fh:
            seqs = [line.strip() for line in fh if line.strip()]

    print(max_hamming_distance(seqs))


if __name__ == "__main__":
    main()
