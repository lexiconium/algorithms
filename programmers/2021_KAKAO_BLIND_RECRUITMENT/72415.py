# https://programmers.co.kr/learn/courses/30/lessons/72415

from collections import defaultdict
import heapq

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def get_cnt(board, r, c, _r, _c):
    cnt_map = [[float('inf') for _ in range(4)] for _ in range(4)]
    cnt_map[r][c] = 0
    
    pq = [(0, r, c)]
    heapq.heapify(pq)
    while pq:
        curr_cnt, curr_r, curr_c = heapq.heappop(pq)
        if curr_r == _r and curr_c == _c:
            return curr_cnt
        
        for d in range(4):
            r, c, cnt = curr_r, curr_c, 0
            while 0 <= r + dr[d] < 4 and 0 <= c + dc[d] < 4:
                r += dr[d]
                c += dc[d]
                cnt += 1
                if board[r][c]:
                    break

                if cnt_map[r][c] > curr_cnt + cnt:
                    cnt_map[r][c] = curr_cnt + cnt
                    heapq.heappush(pq, (curr_cnt + cnt, r, c))

            if cnt_map[r][c] > curr_cnt + 1:
                cnt_map[r][c] = curr_cnt + 1
                heapq.heappush(pq, (curr_cnt + 1, r, c))
            
def get_min_cnt(board, r, c):
    if not sum(map(sum, board)):
        return 0
    min_cnt = float('inf')
    
    locations = defaultdict(list)
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col]:
                locations[board[row][col]].append((row, col))

    for card in locations.keys():
        (r1, c1), (r2, c2) = locations[card]
        
        cnt12 = get_cnt(board, r1, c1, r2, c2) + 2
        cnt1 = get_cnt(board, r, c, r1, c1) + cnt12
        cnt21 = get_cnt(board, r2, c2, r1, c1) + 2
        cnt2 = get_cnt(board, r, c, r2, c2) + cnt21

        board[r1][c1] = board[r2][c2] = 0
        min_cnt = min(
            min_cnt,
            cnt1 + get_min_cnt(board, r2, c2),
            cnt2 + get_min_cnt(board, r1, c1)
        )
        board[r1][c1] = board[r2][c2] = card
        
    return min_cnt

def solution(board, r, c):
    return get_min_cnt(board, r, c)