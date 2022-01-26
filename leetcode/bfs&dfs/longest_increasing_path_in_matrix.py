# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]


class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        self.row = len(matrix)
        self.col = len(matrix[0])

        self.cache = [[0 for _ in row] for row in matrix]

        max_cnt = 1
        for r in range(self.row):
            for c in range(self.col):
                if self.cache[r][c]:
                    continue
                max_cnt = max(self.dfs(matrix, r, c), max_cnt)
        return max_cnt

    def dfs(self, matrix: list[list[int]], r: int, c: int, cnt: int = 1) -> int:
        max_cnt = cnt
        for _r, _c in [(r + _dr, c + _dc) for _dr, _dc in zip(dr, dc)]:
            if 0 <= _r < self.row and 0 <= _c < self.col:
                if matrix[_r][_c] > matrix[r][c]:
                    max_cnt = max(self.dfs(matrix, _r, _c, cnt + 1), max_cnt)

        if not self.cache[r][c]:
            self.cache[r][c] = max_cnt - cnt + 1

        return max_cnt
