# https://leetcode.com/problems/linked-list-cycle-ii/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode | None) -> ListNode | None:
        if head is None:
            return

        node = head
        visited = {id(node): node}

        while node.next is not None:
            node = node.next

            if (node_id := id(node)) in visited:
                return visited[node_id]

            visited[node_id] = node

        return

    def detectCycle(self, head: ListNode | None) -> ListNode | None:
        node = head
        visited = set()

        while node:
            if node in visited:
                return node

            visited.add(node)
            node = node.next
