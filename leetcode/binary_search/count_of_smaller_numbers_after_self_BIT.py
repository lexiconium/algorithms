# https://leetcode.com/problems/count-of-smaller-numbers-after-self/
# https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/76731/Nlogn-Python-solution-binary-indexed-tree-160-ms
# https://www.hackerearth.com/practice/data-structures/advanced-data-structures/fenwick-binary-indexed-trees/tutorial/

# time complexity: O(nlog(n))

class Solution:
    class BIT:
        def __init__(self, _len: int):
            self.len = _len + 1
            self.tree = [0] * self.len
        
        def update(self, rank: int):
            while rank < self.len:
                self.tree[rank] += 1
                rank += rank & -rank

        def query(self, rank: int) -> int:
            s = 0
            while rank:
                s += self.tree[rank]
                rank -= rank & -rank
            return s

    def countSmaller(self, nums: list[int]) -> list[int]:
        ranks = {n: i for i, n in enumerate(sorted(set(nums)), 1)}
        tree = self.BIT(len(ranks))

        cnt = [0] * (_len := len(nums))
        for i in range(_len)[::-1]:
            cnt[i] = tree.query(ranks[nums[i]] - 1)
            tree.update(ranks[nums[i]])
        return cnt