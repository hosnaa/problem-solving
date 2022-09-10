# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
#         new_head = ListNode(-2) # for traversing the whole list and not missing the 1st
#         new_head.next = head
        
#         while head.next:
#             if head.next.val == val:
#                 head.next = head.next.next # then we would skip one
#                 # head.val = None
#             else:
#                 head = head.next # else "move" normally to the next
            
#         return new_head.next
            new_head_copy = ListNode(-1) # to be able to start (.next) from the beginning of head (not to miss the 1st element while making .next)
            new_head_copy.next = head 

            cur_node = new_head_copy # we want this "new_head" to remain in the first pointer/first place
            while cur_node.next: # can start safely by .next as the 1st is an irrelevant number
                if cur_node.next.val == val:
                    cur_node.next = cur_node.next.next
                    # head.val = None
                else:
                    cur_node = cur_node.next
            #     head = head.next
            #     new_head = new_head.next
            #     print(new_head.val)
            # if head.val == val:
            #     new_head.next = None

            return new_head_copy.next
        