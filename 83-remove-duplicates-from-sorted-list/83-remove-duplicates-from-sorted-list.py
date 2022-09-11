# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        while head: # not head.next as if it's none then it'll yield error of not having next
            if head.next and head.val == head.next.val: # checking head.next as you're checking for its value
                head.next = head.next.next
            else:
                head = head.next # This is only at else not for all => as if we found duplicates; we'd return again
                ## to the first non-duplicate and compare with coming (not leave it unless no coming equals to it)
                ## to account for having more than 1 duplicate
            # temp.next = head ## Remmeber they're pointers; both pointing to same; thus any change in one reflects on the other
            ## if we kept the previous line it'll skip sth in middle
        return temp # head points to None now as it gets updated, we return what's not getting updated; what is just pointing to the changes


        