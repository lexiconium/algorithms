# https://leetcode.com/problems/smallest-missing-genetic-value-in-each-subtree/description/


class Solution:
    def smallestMissingValueSubtree(
        self, parents: list[int], nums: list[int]
    ) -> list[int]:
        is_seen = [False] * 100002

        children = [[] for _ in nums]
        for child, parent in enumerate(parents):
            if parent == -1:
                continue

            children[parent].append(child)

        def dfs(node: int) -> None:
            if is_seen[num := nums[node]]:
                return

            is_seen[num] = True
            for child in children[node]:
                dfs(child)

        ans = [1] * len(nums)

        try:
            node = nums.index(1)
        except:
            return ans

        num_missing = 1

        while node > -1:
            dfs(node)

            while is_seen[num_missing]:
                num_missing += 1

            ans[node] = num_missing
            node = parents[node]

        return ans
