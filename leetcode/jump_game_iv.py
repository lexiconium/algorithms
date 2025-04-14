# https://leetcode.com/problems/jump-game-iv/description/


from collections import defaultdict, deque


class Solution:
    def minJumps(self, arr: list[int]) -> int:
        value_indices = defaultdict(list)
        for i, n in enumerate(arr):
            value_indices[n].append(i)

        n = len(arr)
        q = deque([(0, 0)])
        visited = {0}

        while q:
            i, steps = q.popleft()

            if i == n - 1:
                return steps

            if i + 1 < n and i + 1 not in visited:
                q.append((i + 1, steps + 1))
                visited.add(i + 1)

            if 0 <= i - 1 and i - 1 not in visited:
                q.append((i - 1, steps + 1))
                visited.add(i - 1)

            for j in reversed(value_indices[value := arr[i]]):
                if j in visited:
                    continue

                q.append((j, steps + 1))
                visited.add(j)

            value_indices.pop(value)
