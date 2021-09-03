# https://leetcode.com/problems/reverse-pairs/
# https://leetcode.com/problems/reverse-pairs/discuss/162757/Python-BIT-using-ranks-Clear-O(nlog(n))

# time complexity: O(nlog(n))

class Solution:
    class BIT:
        def __init__(self, _len: int):
            self._len = _len + 1
            self.tree = [0] * self._len
        
        def update(self, rank: int):
            while rank < self._len:
                self.tree[rank] += 1
                rank += rank & -rank
        
        def query(self, rank: int) -> int:
            s = 0
            while rank:
                s += self.tree[rank]
                rank -= rank & -rank
            return s
        
    def reversePairs(self, nums: list[int]) -> int:
        _nums = nums + [2 * n for n in nums]
        ranks = {n: rank for rank, n in enumerate(sorted(set(_nums)), 1)}
        
        tree, cnt = self.BIT(len(ranks)), 0
        for n in nums[::-1]:
            cnt += tree.query(ranks[n] - 1)
            tree.update(ranks[2 * n])
        return cnt