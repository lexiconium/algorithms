# https://leetcode.com/problems/find-the-winner-of-an-array-game/description/


from collections import deque


class Solution:
    def getWinner(self, arr: list[int], k: int) -> int:
        if k >= len(arr) - 1:
            return max(arr)

        n, *arr = arr
        arr = deque(arr)

        cnt = 0

        while cnt < k:
            if n > arr[0]:
                arr.append(arr.popleft())
                cnt += 1
            else:
                arr.append(n)
                n = arr.popleft()
                cnt = 1

        return n

    def getWinner(self, arr: list[int], k: int) -> int:
        num_max = max(arr)
        m, *arr = arr
        cnt = 0

        for n in arr:
            if n < m:
                cnt += 1
            else:
                m = n
                cnt = 1

            if cnt == k or m == num_max:
                return m
