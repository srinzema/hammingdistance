#!/usr/bin/env python3
from typing import List
from itertools import combinations


def hamming_distance(seq1: str, seq2: str) -> int:
    """Calculate the Hamming distance between two sequences."""
    return sum(n1 != n2 for n1, n2 in zip(seq1, seq2))


def max_hamming_distance(sequences: List[str]) -> int:
    """Calculate the maximum Hamming distance among a list of sequences."""
    return max(hamming_distance(a, b) for a, b in combinations(sequences, 2))
