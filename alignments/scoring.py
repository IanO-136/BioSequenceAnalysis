from typing import Dict, Tuple

BLOSUM62: Dict[Tuple[str, str], int] = {}

def _seed_blosum():
    entries = {
        ('A','A'): 4,  ('A','R'): -1, ('A','N'): -2, ('A','D'): -2, ('A','C'): 0,  ('A','Q'): -1, ('A','E'): -1, ('A','G'): 0,  ('A','H'): -2, ('A','I'): -1,
        ('R','R'): 5,  ('R','N'): 0,  ('R','D'): -2, ('R','C'): -3, ('R','Q'): 1,  ('R','E'): 0,  ('R','G'): -2, ('R','H'): 0,  ('R','I'): -3,
        ('N','N'): 6,  ('N','D'): 1,  ('N','C'): -3, ('N','Q'): 0,  ('N','E'): 0,  ('N','G'): 0,  ('N','H'): 1,  ('N','I'): -3,
        ('D','D'): 6,  ('D','C'): -3, ('D','Q'): 0,  ('D','E'): 2,  ('D','G'): -1, ('D','H'): -1, ('D','I'): -3,
        ('C','C'): 9,  ('C','Q'): -3, ('C','E'): -4, ('C','G'): -3, ('C','H'): -3, ('C','I'): -1,
        ('Q','Q'): 5,  ('Q','E'): 2,  ('Q','G'): -2, ('Q','H'): 0,  ('Q','I'): -3,
        ('E','E'): 5,  ('E','G'): -2, ('E','H'): 0,  ('E','I'): -3,
        ('G','G'): 6,  ('G','H'): -2, ('G','I'): -4,
        ('H','H'): 8,  ('H','I'): -3,
        ('I','I'): 4,
    }
    for (a, b), val in entries.items():
        BLOSUM62[(a, b)] = val
        BLOSUM62[(b, a)] = val

_seed_blosum()


def dna_score(a: str, b: str, match: int = 1, mismatch: int = -1) -> int:
    aa = a.upper()
    bb = b.upper()
    if len(aa) == 0 or len(bb) == 0:
        return mismatch
    if aa == bb:
        return match
    return mismatch


def blosum62(a: str, b: str, fallback: int = -1) -> int:
    aa = a.upper()
    bb = b.upper()
    if (aa, bb) in BLOSUM62:
        return BLOSUM62[(aa, bb)]
    if (bb, aa) in BLOSUM62:
        return BLOSUM62[(bb, aa)]
    return fallback
