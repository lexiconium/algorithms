# https://programmers.co.kr/learn/courses/30/lessons/84021

def rotate_block(block):
    return [row[::-1] for row in zip(*block)]

def fit_to_block(block):
    r_min = c_min = len(block)
    r_max = c_max = 0
    for r, row in enumerate(block):
        for c, val in enumerate(row):
            if val:
                r_min, r_max = min(r_min, r), max(r_max, r)
                c_min, c_max = min(c_min, c), max(c_max, c)
    
    return [row[c_min:c_max + 1] for row in block[r_min:r_max + 1]]

def is_in(r, c, table):
    return 0 <= r < len(table) and 0 <= c < len(table[0])

def is_valid(r, c, table):
    return is_in(r, c, table) and table[r][c]

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
    blocks = []
    for r, row in enumerate(table):
        for c, val in enumerate(row):
            if val:
                blocks.append(return_block(table, r, c))
    return blocks

def fill_board(r_ref, c_ref, game_board, block):
    cnt = 0
    for r, row in enumerate(block):
        for c, val in enumerate(row):
            if val:
                _r, _c = r_ref + r, c_ref + c
                if not is_in(_r, _c, game_board) or game_board[_r][_c]:
                    return 0
                cnt += 1
    return cnt

def cnt_holes(r, c, game_board):
    board = [row for row in game_board]
    cnt = 0
    stk = [(r, c)]
    while stk:
        r, c = stk.pop()
        board[r][c] = 1
        cnt += 1
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            _r, _c = r + dr, c + dc
            if is_in(_r, _c, board) and not board[_r][_c]:
                stk.append((_r, _c))
    return cnt, board

def does_fit(r, c, game_board, blocks):
    for idx, block in enumerate(blocks):
        for n_rot in range(4):
            if n_rot:
                block = rotate_block(block)
            if cnt := fill_board(r, c, game_board, block):
                holes, board = cnt_holes(r, c, game_board)
                if holes == cnt:
                    blocks.pop(idx)
                    return cnt
    return 0

def solution(game_board, table):
    n_fill = 0
    blocks = extract_blocks(table)
    for r, row in enumerate(game_board):
        for c, val in enumerate(row):
            if val:
                continue
            n_fill += does_fit(r, c, game_board, blocks)
    return n_fill
