# https://leetcode.com/problems/surrounded-regions/description/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        os = []

        for r, row in enumerate(board):
            for c, v in enumerate(row):
                if v == "O":
                    os.append((r, c))

        def is_valid(r: int, c: int) -> bool:
            return 0 <= r < len(board) and 0 <= c < len(board[r])

        def bfs(point: Tuple[int, int]) -> Tuple[set, bool]:
            q = deque([point])
            visited = {point}

            is_captured = True

            while q:
                r, c = q.popleft()

                for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    if not is_valid(nr := r + dr, nc := c + dc):
                        is_captured = False
                        continue
                    if board[nr][nc] == "X":
                        continue
                    if (nr, nc) in visited:
                        continue

                    q.append((nr, nc))
                    visited.add((nr, nc))

            return visited, is_captured

        visited = set()

        for point in os:
            if point in visited:
                continue

            group, is_captured = bfs(point)

            if is_captured:
                for r, c in group:
                    board[r][c] = "X"

            visited |= group
