# You are given the head of a singly linked-list.

# The positions of a linked list of length = 7 for example, can intially be represented as:

# [0, 1, 2, 3, 4, 5, 6]

# Reorder the nodes of the linked list to be in the following order:

# [0, 6, 1, 5, 2, 4, 3]

# Notice that in the general case for a list of length = n the nodes are reordered to be in the following order:

# [0, n-1, 1, n-2, 2, n-3, ...]



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head or not head.next:
            return
        #if there is no values in the list

        slow,fast = head,head #two pointers start at the started of the LinkedList
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        secondList = slow.next #slow is middle now since fast is out of bounds and slow will land in N/2 i.e the half 
                                #so the next is the later half of the list to be alternated
        slow.next = None #breaking the linkedlist

        #NOW REVERSING THE SECOND HALF

        prev = None
        curr = secondList

        while curr: #while current node is not out of bounds
            temp = curr.next
            curr.next = prev
            prev = curr 
            curr = temp 
        
        secondList = prev #make the second half reverse List new head updated

        first, second = head, secondList
        while second:
            tmp1, tmp2 = first.next, second.next  #save the next pointers
            first.next = second  #first will have next pointer to the next half first
            second.next = tmp1  #second will have the the next pointer to first half
            first, second = tmp1, tmp2  #update first and second to be their next nodes

        
            











        