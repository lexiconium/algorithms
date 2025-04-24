# https://leetcode.com/problems/node-with-highest-edge-score/description/


class Solution:
    def edgeScore(self, edges: list[int]) -> int:
        scores = [0] * len(edges)

        for i, j in enumerate(edges):
            scores[j] += i

        return scores.index(max(scores))
