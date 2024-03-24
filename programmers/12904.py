def solution(s):
    dp = [[False] * len(s) for _ in s]

    max_len = 1

    for begin in reversed(range(len(s))):
        dp[begin][begin] = True

        for end in range(begin + 1, len(s)):
            is_palindrome = s[begin] == s[end]

            if end - begin > 1:
                is_palindrome &= dp[begin + 1][end - 1]

            dp[begin][end] = is_palindrome

            if is_palindrome:
                max_len = max(end - begin + 1, max_len)

    return max_len
