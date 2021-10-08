# https://programmers.co.kr/learn/courses/30/lessons/84021

def rotate_block(block):
    return [row[::-1] for row in zip(*block)]

def fit_to_block(block):
    r_min = c_min = len(block)
    r_max = c_max = 0
    for ridx, row in enumerate(block):
        for cidx, val in enumerate(row):
            if val:
                r_min, r_max = min(r_min, ridx), max(r_max, ridx)
                c_min, c_max = min(c_min, cidx), max(c_max, cidx)
    
    return [row[c_min:c_max] for row in block[r_min:r_max]]

def is_valid(r, c, table):
    return 0 <= r < len(table) and 0 <= c < len(table[0]) and table[r][c]

def return_block(table, ref_r, ref_c):
    block = [[0 for _ in table[0]] for _ in table]
    stk = [(ref_r, ref_c)]
    while stk:
        r, c = stk.pop()
        table[r][c] = 0
        block[r][c] = 1
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            _r, _c = r + dr, c + dc
            if is_valid(_r, _c, table):
                stk.append((_r, _c))
    
    return fit_to_block(block)

def extract_blocks(table):
    # return [
    #     return_block(table, ridx, cidx) for cidx, val in enumerate(row)
    #     for ridx, row in enumerate(table) if val
    # ]

    blocks = []
    for ridx, row in enumerate(table):
        for cidx, val in enumerate(row):
            if val:
                blocks.append(return_block(table, ridx, cidx))
    return blocks

def solution(game_board, table):
    print(extract_blocks(table))
