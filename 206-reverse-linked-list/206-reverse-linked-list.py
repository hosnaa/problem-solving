# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# reverse = ListNode(None)
## The main idea is to change the pointers (not as in the image); we won't change the node or the values, just the pointers

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            temp = head
            head = head.next
            temp.next = prev # we can't return temp for this line; assigning sth to None.next
            prev = temp
        return prev
        