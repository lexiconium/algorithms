# https://leetcode.com/problems/count-the-number-of-good-nodes/

from collections import defaultdict
from functools import cache


class Solution:
    def countGoodNodes(self, edges: list[list[int]]) -> int:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        @cache
        def get_size(node: int, p_of_node: int = -1) -> int:
            if not graph[node]:
                return 1
            return 1 + sum(get_size(c, node) for c in graph[node] if c != p_of_node)

        def count(node: int, p_of_node: int = -1) -> int:
            if not graph[node]:
                return 1

            size = -1
            allequal = 1

            for c in graph[node]:
                if c == p_of_node:
                    continue

                if size == -1:
                    size = get_size(c, node)
                elif size != get_size(c, node):
                    allequal = 0

            return allequal + sum(count(c, node) for c in graph[node] if c != p_of_node)

        return count(0)


class Solution:
    def countGoodNodes(self, edges: list[list[int]]) -> int:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node: int, parent: int = -1) -> tuple[int, int]:
            total_size = 1
            good_count = 0
            child_sizes = []

            for child in graph[node]:
                if child == parent:
                    continue
                subtree_size, child_good = dfs(child, node)
                total_size += subtree_size
                good_count += child_good
                child_sizes.append(subtree_size)

            if len(child_sizes) <= 1 or all(s == child_sizes[0] for s in child_sizes):
                good_count += 1

            return total_size, good_count

        return dfs(0)[1]
