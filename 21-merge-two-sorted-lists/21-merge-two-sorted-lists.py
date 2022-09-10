# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# https://leetcode.com/problems/merge-two-sorted-lists/discuss/759870/Python3-Solution-with-a-Detailed-Explanation-dummy-explained
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = list1
        head2 = list2
        merge = merge_copy = ListNode()
        # if head1:
        #     merge.next = head1
        # if head2: 
        #     merge.next = head2
        while head1 and head2:
            if head1.val < head2.val:
                merge.next = head1
                head1 = head1.next
                # print(merge.val)
            else:
                merge.next = head2
                head2 = head2.next
                # print(merge.val)
            merge = merge.next # move to add to the following next pointer not change the current next (like heads)
        if head1 or head2: 
            merge.next = head1 if head1 else head2
            
        return merge_copy.next # copy not merge itself as merge itself will be the last next not full (from merge=merge.next); again like head at the end will have only the last
        
        