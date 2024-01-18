# https://leetcode.com/problems/filling-bookcase-shelves/


class Solution:
    def minHeightShelves(self, books: list[list[int]], shelfWidth: int) -> int:
        dp = [0] + [float("inf")] * (num_books := len(books))

        for i in range(1, num_books + 1):
            filled = height = 0

            for j in reversed(range(i)):
                book_width, book_height = books[j]

                if (filled := filled + book_width) > shelfWidth:
                    break

                dp[i] = min(dp[j] + (height := max(book_height, height)), dp[i])

        return dp[-1]
