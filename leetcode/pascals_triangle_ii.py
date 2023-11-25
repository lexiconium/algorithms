# https://leetcode.com/problems/pascals-triangle-ii/description/

class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex < 2:
            return [1] * (rowIndex + 1)

        rm2, rm1 = [1], [1, 1]

        for _ in range(rowIndex - 1):
            rm2, rm1 = rm1, [
                1 if i == 0 or i == len(rm1) else rm1[i - 1] + rm1[i]
                for i in range(len(rm1) + 1)
            ]

        return rm1
