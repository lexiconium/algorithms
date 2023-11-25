# https://leetcode.com/problems/remove-linked-list-elements/description/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy_node = ListNode(next=head)

        prev_node, node = dummy_node, head

        while node is not None:
            if node.val == val:
                prev_node.next = node.next
            else:
                prev_node = node

            node = node.next

        return dummy_node.next
