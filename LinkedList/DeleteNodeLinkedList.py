# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if head is None:
            return None #no list exists edge case

        #Maybe the approach here should be the fact that we should make two pointers to traverse through the linked list and the other pointer
        #should always be n distance behind after one reaches end

        Dummy = ListNode(0,head) #value and next i.e head
        left = Dummy
        right = head #left will be behind to fetch the previous value when it goes out of bounds

        while n>0 and right:
            right = right.next 
            n = n-1
        #move the sliding LN window with right first ahead

        while right:
            left = left.next 
            right = right.next 
        #will always have one more than n gap like this

        left.next = left.next.next #deleting the node by unlinking from target to be del to the one after it 

        return Dummy.next #incase head is deleted




        