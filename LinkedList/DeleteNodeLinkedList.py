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

        ToBeDeleted = head
        OutBounder = head

        while OutBounder and OutBounder.next: #while the pointer that will go out of bounds still still here 

            for i in range(n):
                OutBounder = OutBounder.next
            #jump n distances ahead first

            ToBeDeleted = ToBeDeleted.next
        
        #now we have found our to be deleted linkedlist
      
        if head == ToBeDeleted:
            return head.next #if head has to be deleted then return from next node onwards

        prev = head
        curr = head.next

        while curr:
            if curr == ToBeDeleted:
                prev.next = curr.next #unlink that node
            prev = curr
            curr = curr.next

        #return the deleted node list now from the head
        
        return head

        



        