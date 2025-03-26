# https://leetcode.com/problems/snake-in-matrix/


class Solution:
    def finalPositionOfSnake(self, n: int, commands: list[str]) -> int:
        i = j = 0

        for di, dj in (
            {"UP": (-1, 0), "RIGHT": (0, 1), "DOWN": (1, 0), "LEFT": (0, -1)}[command]
            for command in commands
        ):
            i += di
            j += dj

        return i * n + j
