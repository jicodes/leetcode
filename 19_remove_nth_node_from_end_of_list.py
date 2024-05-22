# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Dummy node to handle edge cases
        dummy = ListNode(0)
        dummy.next = head

        # Calculate the length of the list
        length = 0
        current = head
        while current:
            length += 1
            current = current.next

        # Calculate the position of the node to be removed from the beginning
        target_index = length - n

        # Traverse the list again to find the node just before the target node
        current = dummy
        for _ in range(target_index):
            current = current.next

        # Remove the target node
        current.next = current.next.next

        return dummy.next
