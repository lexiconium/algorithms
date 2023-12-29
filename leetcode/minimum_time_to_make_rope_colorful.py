# https://leetcode.com/problems/minimum-time-to-make-rope-colorful/


class Solution:
    def minCost(self, colors: str, needed_time: list[int]) -> int:
        stack = [(colors[0], needed_time[0])]
        total = 0

        for i in range(1, len(colors)):
            color, time = stack[-1]

            if (next_color := colors[i]) != color:
                stack.append((next_color, needed_time[i]))
                continue

            if time < (next_time := needed_time[i]):
                stack[-1] = (next_color, next_time)
                total += time
            else:
                total += next_time

        return total

    # https://leetcode.com/problems/minimum-time-to-make-rope-colorful/solutions/831588/java-c-python-straight-forward/
    def minCost(self, colors: str, needed_time: list[int]) -> int:
        total = 0
        max_group_t = needed_time[0]

        for i in range(1, len(colors)):
            if colors[i - 1] != colors[i]:
                max_group_t = 0

            total += min(needed_time[i], max_group_t)
            max_group_t = max(needed_time[i], max_group_t)

        return total
