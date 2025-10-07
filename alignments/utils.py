from typing import List, Tuple
import numpy as np
import matplotlib.pyplot as plt

def to_numpy(matrix: List[List[int]]):
    return np.array(matrix, dtype=float)

def draw_matrix(matrix: List[List[int]], path_cells: Tuple[Tuple[int,int], ...] = None, title: str = "", reveal_until: int = None):
    data = to_numpy(matrix)

    if reveal_until is not None:
        pass

    fig, ax = plt.subplots(figsize=(6, 6))
    im = ax.imshow(data, aspect='auto')
    ax.set_title(title)
    ax.set_xlabel("Sequence B (columns)")
    ax.set_ylabel("Sequence A (rows)")
    fig.colorbar(im, ax=ax, shrink=0.8)

    if path_cells is not None:
        index = 0
        while index < len(path_cells):
            (r, c) = path_cells[index]
            ax.scatter([c], [r], s=30)
            index = index + 1

    ax.invert_yaxis()
    fig.tight_layout()
    return fig

def path_from_directions(direction, end_r, end_c):
    cells = []
    r = end_r
    c = end_c
    cells.append((r, c))
    while r > 0 or c > 0:
        move = direction[r][c]
        if move == 'diag':
            r = r - 1
            c = c - 1
        elif move == 'up':
            r = r - 1
        elif move == 'left':
            c = c - 1
        else:
            break
        cells.append((r, c))
    cells.reverse()
    return tuple(cells)
