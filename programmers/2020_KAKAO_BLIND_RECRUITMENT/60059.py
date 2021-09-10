# https://programmers.co.kr/learn/courses/30/lessons/60059

def get_necessary(lock, target):
    min_row, max_row = len(lock) - 1, 0
    min_col, max_col = len(lock[0]) - 1, 0
    for row_i, row in enumerate(lock):
        for col_i, val in enumerate(row):
            if val == target:
                min_row = min(min_row, row_i)
                min_col = min(min_col, col_i)
                max_row = max(max_row, row_i)
                max_col = max(max_col, col_i)
    
    return [lock[row_i][min_col:max_col + 1] for row_i in range(min_row, max_row + 1)]

def rotate90cw(lock):
    return list(map(lambda col_vec: col_vec[::-1], zip(*lock)))

def find(lock, key):
    for row_i in range(len(key) - len(lock) + 1):
        for col_i in range(len(key[0]) - len(lock[0]) + 1):
            does_fit = True
            for nth_row, row in enumerate(key[row_i:row_i + len(lock)]):                
                if row[col_i:col_i + len(lock[0])] != list(map(lambda x: x^1, lock[nth_row])):
                    does_fit = False
                    break
            if does_fit:
                return True
    return False

def solution(key, lock):
    if sum(sum(row) for row in lock) == len(lock) * len(lock[0]):
        return True
    
    key = get_necessary(key, target=1)
    lock = get_necessary(lock, target=0)
    
    for rotate in range(4):
        if rotate:
            lock = rotate90cw(lock)
        if find(lock, key):
            return True
    return False
