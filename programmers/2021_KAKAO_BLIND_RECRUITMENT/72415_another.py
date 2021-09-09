# https://programmers.co.kr/learn/courses/30/lessons/72415

from itertools import permutations
from collections import deque, defaultdict

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def ctrl(board, r, c, d):
    for _ in range(4):
        r += dr[d]
        c += dc[d]
        if 0 <= r < 4 and 0 <= c < 4:
            if board[r][c]:
                return (r, c)
        else:
            return (r - dr[d], c - dc[d])

def move(board, loc1, loc2):
    dist_map = [[float('inf') for _ in range(4)] for _ in range(4)]
    q = deque([(loc1, 0)])
    while q:
        (r, c), dist = q.popleft()
        if dist < dist_map[r][c]:
            dist_map[r][c] = dist
            for d in range(4):
                if 0 <= r + dr[d] < 4 and 0 <= c + dc[d] < 4:
                    q.append(((r + dr[d], c + dc[d]), dist + 1))
                    q.append((ctrl(board, r, c, d), dist + 1))
                    
    return dist_map[loc2[0]][loc2[1]]

def solution(board, r, c):
    card_locs = defaultdict(list)
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]:
                card_locs[board[i][j]].append((i, j))
    
    min_cnt = float('inf')
    for permut in permutations(card_locs.values()):
        cnt = 0
        locs = [(r, c)]
        _board = [[v for v in row] for row in board]
        for loc1, loc2 in permut:
            dist_and_loc = [(move(_board, loc, loc1) + move(_board, loc1, loc2), loc2) for loc in locs] + \
                           [(move(_board, loc, loc2) + move(_board, loc2, loc1), loc1) for loc in locs]
            _board[loc1[0]][loc1[1]] = _board[loc2[0]][loc2[1]] = 0
            min_dist = min(dist_and_loc)[0]
            cnt += min_dist + 2
            locs = [loc for dist, loc in dist_and_loc if dist == min_dist]
        min_cnt = min(min_cnt, cnt)
        
    return min_cnt
