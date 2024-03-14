# https://leetcode.com/problems/count-submatrices-with-all-ones/description/


class Solution:
    def numSubmat(self, mat: list[list[int]]) -> int:
        num_rows, num_cols = len(mat), len(mat[0])

        for r in range(1, num_rows):
            for c in range(num_cols):
                if not mat[r][c]:
                    continue

                mat[r][c] += mat[r - 1][c]

        total_cnt = 0

        for r in range(num_rows):
            stack = []
            cnt = 0

            for c in range(num_cols):
                while stack and (height_left := mat[r][stack[-1]]) > (
                    height := mat[r][c]
                ):
                    left = stack.pop()
                    lleft = stack[-1] if stack else -1

                    # heights between left and lleft must be higher than left.
                    # those heights are already been dealt when the index c was left, i.e.,
                    # height_left * (left - lleft) is added to the cnt.
                    # therefore extract (height_left - height) * (left - lleft).
                    cnt -= (height_left - height) * (left - lleft)

                cnt += mat[r][c]
                total_cnt += cnt

                stack.append(c)

        return total_cnt
