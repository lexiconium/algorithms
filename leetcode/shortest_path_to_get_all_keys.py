# https://leetcode.com/problems/shortest-path-to-get-all-keys/

# time complexity:

class Solution:
    def shortestPathAllKeys(self, grid: list[str]) -> int:
        get_key = lambda c: 1 << (ord(c) - ord('a'))
        keys = 0
        for i in range(m := len(grid)):
            for j in range(n := len(grid[0])):
                if grid[i][j] == '@':
                    i_start, j_start = i, j
                elif grid[i][j].islower():
                    keys += get_key(grid[i][j])
        
        q = [(i_start, j_start, 0)]
        visited = set(q)
        moves = 0
        while q:
            next_q = []
            for i, j, _keys in q:
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    r, c = i + di, j + dj
                    if 0 <= r < m and 0 <= c < n and grid[r][c] != '#':
                        if grid[r][c].islower() and not _keys & get_key(grid[r][c]):
                            updated_keys = _keys + get_key(grid[r][c])
                            if updated_keys == keys:
                                return moves + 1
                            visited.add((r, c, updated_keys))
                            next_q.append((r, c, updated_keys))
                        elif (grid[r][c] in ".@" or _keys & get_key(grid[r][c].lower())) and (r, c, _keys) not in visited:
                            visited.add((r, c, _keys))
                            next_q.append((r, c, _keys))
            q = next_q
            moves += 1
        return -1