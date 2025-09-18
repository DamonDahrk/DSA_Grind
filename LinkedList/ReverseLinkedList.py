# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        #initilize the pointers
        
        while curr:
            t = curr.next
            curr.next = prev
            prev = curr
            curr = t
        
        #loop keeps going to reverse with help of temp node t till curr goes out of bounds

        return prev
        
        #prev is the new head then
        