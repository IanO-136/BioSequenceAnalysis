from typing import List, Tuple, Callable

def smith_waterman(seq_a: str, seq_b: str, score_fn: Callable[[str, str], int], gap_penalty: int = -2):
    letters_a = list(seq_a)
    letters_b = list(seq_b)
    rows = len(letters_a) + 1
    cols = len(letters_b) + 1

    dp = []
    direction = []  # 'diag', 'up', 'left', or '' for zero reset
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

    max_r = 0
    max_c = 0
    max_val = 0

    r = 1
    fill_order = []
    while r < rows:
        c = 1
        while c < cols:
            score_diag = dp[r-1][c-1] + score_fn(letters_a[r-1], letters_b[c-1])
            score_up = dp[r-1][c] + gap_penalty
            score_left = dp[r][c-1] + gap_penalty

            best = 0
            best_dir = ''

            if score_diag > best:
                best = score_diag
                best_dir = 'diag'
            if score_up > best:
                best = score_up
                best_dir = 'up'
            if score_left > best:
                best = score_left
                best_dir = 'left'

            dp[r][c] = best
            direction[r][c] = best_dir
            fill_order.append((r, c))

            if best > max_val:
                max_val = best
                max_r = r
                max_c = c

            c = c + 1
        r = r + 1

    # Traceback from max cell until zero
    align_a = []
    align_b = []
    r = max_r
    c = max_c
    while r > 0 and c > 0 and dp[r][c] > 0:
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
        elif move == 'left':
            align_a.append('-')
            align_b.append(letters_b[c-1])
            c = c - 1
        else:
            break

    align_a.reverse()
    align_b.reverse()

    return dp, direction, ''.join(align_a), ''.join(align_b), fill_order, (max_r, max_c)
