# https://leetcode.com/problems/minimum-sideway-jumps/


class Solution:
    def minSideJumps(self, obstacles: list[int]) -> int:
        prev = [float("inf")] * 3
        curr = [0] * 3

        for i in reversed(range(1, len(obstacles))):
            for lane in range(3):
                if obstacles[i] != lane + 1:
                    prev[lane] = curr[lane]
                else:
                    if obstacles[i - 1] != (adj := (lane + 1) % 3) + 1:
                        prev[lane] = curr[adj] + 1
                    if obstacles[i - 1] != (adj := (lane + 2) % 3) + 1:
                        prev[lane] = min(curr[adj] + 1, prev[lane])

            prev, curr = [float("inf")] * 3, prev

        return curr[1]

    # o1
    def minSideJumps(self, obstacles: list[int]) -> int:
        # Initialize the minimum side jumps for each lane at position 0
        # dp[0], dp[1], dp[2] correspond to lanes 1, 2, and 3 respectively
        dp = [1, 0, 1]  # Starting from lane 2 with 0 side jumps

        for i in range(1, len(obstacles)):
            # Set the side jumps to infinity for lanes with obstacles at position i
            for lane in range(3):
                if obstacles[i] == lane + 1:
                    dp[lane] = float("inf")

            # Update the minimum side jumps for lanes without obstacles
            min_jump = min(dp)
            for lane in range(3):
                if obstacles[i] != lane + 1:
                    # Either stay in the same lane or side jump from another lane
                    dp[lane] = min(dp[lane], min_jump + 1)

        # Return the minimum side jumps needed to reach the end
        return min(dp)
