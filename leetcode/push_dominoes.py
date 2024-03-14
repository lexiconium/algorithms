# https://leetcode.com/problems/push-dominoes/description/


A_LARGE_NUMBER = 100_001


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        to_right_state = [0] * (n := len(dominoes))

        if dominoes[0] == "R":
            to_right_state[0] = A_LARGE_NUMBER

        for i in range(1, n):
            if dominoes[i] == "R":
                to_right_state[i] = A_LARGE_NUMBER
            elif dominoes[i] == "L":
                to_right_state[i] = 0
            elif to_right_state[i - 1] != 0:
                to_right_state[i] = to_right_state[i - 1] - 1

        to_left_state = [0] * n

        if dominoes[-1] == "L":
            to_left_state[-1] = -A_LARGE_NUMBER

        for i in reversed(range(n - 1)):
            if dominoes[i] == "R":
                to_left_state[i] = 0
            elif dominoes[i] == "L":
                to_left_state[i] = -A_LARGE_NUMBER
            elif to_left_state[i + 1] != 0:
                to_left_state[i] = to_left_state[i + 1] + 1

        def to_str(m: int) -> str:
            if m > 0:
                return "R"
            if m < 0:
                return "L"
            return "."

        return "".join(to_str(a + b) for a, b in zip(to_right_state, to_left_state))

    # https://leetcode.com/problems/push-dominoes/solutions/132332/java-c-python-two-pointers/
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = "L" + dominoes + "R"
        state = ""

        left = 0

        for right in range(1, len(dominoes)):
            if dominoes[right] == ".":
                continue

            if left > 0:
                state += dominoes[left]

            in_between = right - left - 1

            if dominoes[left] == dominoes[right]:
                state += dominoes[left] * in_between
            elif dominoes[left] == "L" and dominoes[right] == "R":
                state += "." * in_between
            else:
                state += (
                    "R" * (in_between // 2)
                    + "." * (in_between % 2)
                    + "L" * (in_between // 2)
                )

            left = right

        return state
