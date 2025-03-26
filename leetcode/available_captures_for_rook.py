# https://leetcode.com/problems/available-captures-for-rook/description/


class Solution:
    def numRookCaptures(self, board: list[list[str]]) -> int:
        pos_rook = None

        for r, row in enumerate(board):
            for c, v in enumerate(row):
                if v == "R":
                    pos_rook = (r, c)
                    break

        cnt = 0

        for dr, dc in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            r, c = pos_rook

            while 0 <= r < 8 and 0 <= c < 8:
                if board[r][c] == "B":
                    break
                if board[r][c] == "p":
                    cnt += 1
                    break

                r += dr
                c += dc

        return cnt
