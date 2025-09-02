#!/usr/bin/env python3
import argparse
from hammingdistance.core import max_hamming_distance


def main() -> None:
    """Parse command line arguments and output the max Hamming distance."""
    parser = argparse.ArgumentParser(
        description="Output max Hamming distance among sequences as integer"
    )
    parser.add_argument(
        "-s", "--sequences", nargs="+", help="List of sequences separated by spaces"
    )
    parser.add_argument("-f", "--file", help="Path to file with one sequence per line")
    args = parser.parse_args()

    if not args.sequences and not args.file:
        parser.error("Provide either --sequences or --file")

    if args.sequences:
        seqs = args.sequences
    else:
        with open(args.file) as fh:
            seqs = [line.strip() for line in fh if line.strip()]

    print(max_hamming_distance(seqs))
