# https://leetcode.com/problems/number-of-provinces/description/


class Solution:
    def findCircleNum(self, is_connected: list[list[int]]) -> int:
        disjoint_set = [i for i in range(len(is_connected))]

        def find(i: int) -> int:
            while disjoint_set[i] != i:
                i = disjoint_set[i]
            
            return i

        for i in range(len(disjoint_set) - 1):
            for j in range(i + 1, len(disjoint_set)):
                if not is_connected[i][j]:
                    continue
                
                if (root_i := find(i)) == (root_j := find(j)):
                    continue
                
                disjoint_set[root_j] = root_i

        return sum(disjoint_set[i] == i for i in range(len(disjoint_set)))