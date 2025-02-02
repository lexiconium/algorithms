# https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nodesBetweenCriticalPoints(self, head: ListNode | None) -> list[int]:
        def is_critical(pp, p, v):
            if pp == -1:
                return False
            return p < pp and p < v or p > pp and p > v

        node = head
        pp = p = -1
        first_loc = prev_loc = -1
        loc = 0
        min_dist, max_dist = float("inf"), -1

        while node:
            if loc >= 2 and is_critical(pp, p, node.val):
                if prev_loc == -1:
                    first_loc = prev_loc = loc - 1
                else:
                    min_dist = min(loc - 1 - prev_loc, min_dist)
                    max_dist = loc - 1 - first_loc

                prev_loc = loc - 1

            pp, p = p, node.val
            node = node.next
            loc += 1

        return [-1 if min_dist == float("inf") else min_dist, max_dist]

    # o1-mini
    def nodesBetweenCriticalPoints(self, head: ListNode | None) -> list[int]:
        # Initialize pointers and variables
        index = 1  # Start indexing from 1 for the second node
        first_cp = -1  # Position of the first critical point
        prev_cp = -1  # Position of the previous critical point
        min_dist = float("inf")  # Initialize minimum distance
        max_dist = -1  # Initialize maximum distance

        # Initialize sliding window pointers
        prev_node = head
        current_node = head.next
        if not current_node:
            return [-1, -1]  # Less than two nodes

        next_node = current_node.next

        while next_node:
            # Check if current_node is a critical point
            if (
                current_node.val > prev_node.val and current_node.val > next_node.val
            ) or (
                current_node.val < prev_node.val and current_node.val < next_node.val
            ):

                if first_cp == -1:
                    first_cp = index  # Record the first critical point

                if prev_cp != -1:
                    distance = index - prev_cp
                    min_dist = min(min_dist, distance)
                    max_dist = (
                        index - first_cp
                    )  # Update max distance based on the first critical point

                prev_cp = index  # Update the previous critical point

            # Move the sliding window forward
            prev_node = current_node
            current_node = next_node
            next_node = next_node.next
            index += 1

        # Determine if at least two critical points were found
        if first_cp != -1 and prev_cp != first_cp:
            return [min_dist, max_dist]
        else:
            return [-1, -1]
