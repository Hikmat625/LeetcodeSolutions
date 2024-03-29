# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head , n: int):
        slow = fast = head
        for _ in range(n):
            fast = fast.next
        while fast.val:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next

        return head

        