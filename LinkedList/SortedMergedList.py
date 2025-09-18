#Input: list1 = [1,2,4], list2 = [1,3,5]

# Output: [1,1,2,3,4,5]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        Dummy = ListNode() #we will store the new merged sorted linked list here 
        curr = Dummy  #currentNode starting off the dummy node

        while list1 and list2: #while list1 and list2 still exist

            if list1.val > list2.val:
                curr.next = list2  #smaller value pointing to head of one of sorted lists
                list2 = list2.next
            else:  #opposite or equal doesnt matter
                curr.next = list1  #smaller value pointing to head of one of sorted lists
                list1 = list1.next
            curr = curr.next  # ✅ advance curr each time
            
        if list1: #if list 2 doesnt exist anymore #outside the loop of while to see one of them ran out
                curr.next = list1 #attach list 1
        elif list2: 
                curr.next = list2 #attach list 2
            
        return Dummy.next #return the true value from head