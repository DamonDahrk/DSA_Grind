# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        Dummy = ListNode() #make a dummy node from where we will iterate
        Dummy.next = head #   |dummy| -> |head| from the main node provided
        fast = Dummy
        slow = Dummy

        while fast and fast.next: #as long as fast and the next value exists and doesnt go out of bounds
            fast = fast.next.next #will skip two nodes
            slow = slow.next #will skip one

            if fast == slow: #if they colliding due to Floys algorithm incase of a circular loop they must have same value once 
                return True
        
        return False #out of bounds i.e no loop present in LinkedList
        
        #o1 time complex