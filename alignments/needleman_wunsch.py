from typing import List, Tuple, Callable

def needleman_wunsch(seq_a: str, seq_b: str, score_fn: Callable[[str, str], int], gap_penalty: int = -1):
    # Initialize DP matrix and pointer matrix
    letters_a = list(seq_a)
    letters_b = list(seq_b)
    rows = len(letters_a) + 1
    cols = len(letters_b) + 1

    dp = []
    direction = []  # 'diag', 'up', 'left'
    row_index = 0
    while row_index < rows:
        new_row = []
        new_dir_row = []
        col_index = 0
        while col_index < cols:
            new_row.append(0)
            new_dir_row.append('')
            col_index = col_index + 1
        dp.append(new_row)
        direction.append(new_dir_row)
        row_index = row_index + 1

    # First row/col init
    c = 0
    while c < cols:
        dp[0][c] = gap_penalty * c
        direction[0][c] = 'left' if c > 0 else ''
        c = c + 1
    r = 0
    while r < rows:
        dp[r][0] = gap_penalty * r
        direction[r][0] = 'up' if r > 0 else ''
        r = r + 1

    r = 1
    fill_order = []
    while r < rows:
        c = 1
        while c < cols:
            score_match = dp[r-1][c-1] + score_fn(letters_a[r-1], letters_b[c-1])
            score_delete = dp[r-1][c] + gap_penalty
            score_insert = dp[r][c-1] + gap_penalty

            best = score_match
            best_dir = 'diag'

            if score_delete > best:
                best = score_delete
                best_dir = 'up'
            if score_insert > best:
                best = score_insert
                best_dir = 'left'

            dp[r][c] = best
            direction[r][c] = best_dir
            fill_order.append((r, c))
            c = c + 1
        r = r + 1

    # Traceback
    align_a = []
    align_b = []
    r = rows - 1
    c = cols - 1
    while r > 0 or c > 0:
        move = direction[r][c]
        if move == 'diag':
            align_a.append(letters_a[r-1])
            align_b.append(letters_b[c-1])
            r = r - 1
            c = c - 1
        elif move == 'up':
            align_a.append(letters_a[r-1])
            align_b.append('-')
            r = r - 1
        else:
            align_a.append('-')
            align_b.append(letters_b[c-1])
            c = c - 1

    align_a.reverse()
    align_b.reverse()

    return dp, direction, ''.join(align_a), ''.join(align_b), fill_order
