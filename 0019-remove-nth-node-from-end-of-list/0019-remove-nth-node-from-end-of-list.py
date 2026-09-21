# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy=ListNode(0,head)
        length=0
        current=head
        while current:
            length+=1
            current=current.next

        b=length-n
        prev=dummy
        for i in range(0,b):
            prev=prev.next
        prev.next=prev.next.next

        return dummy.next
