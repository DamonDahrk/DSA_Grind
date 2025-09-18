# You are given two non-empty linked lists, l1 and l2, where each represents a non-negative integer.

# The digits are stored in reverse order, e.g. the number 123 is represented as 3 -> 2 -> 1 -> in the linked list.

# Each of the nodes contains a single digit. You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Return the sum of the two numbers as a linked list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        Dummy = ListNode()  #to deal with some edge cases here 
        curr = Dummy

        carry = 0 #for two digit additions

        while l1 or l2 or carry: #carry has to exist for an edge case if carry cannot be added anymore 
            v1 = l1.val if l1 else 0 #if list still there then add the value else add 0
            v2 = l2.val if l2 else 0
            

            value = v1+v2+carry #adding the value from back as seen here
            carry = value//10 #if result is 15 or any two digit then tens place is carried to carry
            value = value%10 # units place remains at value 
            curr.next = ListNode(value) #create Linked Node with our value and attach it here 

            #UPDATE POINTERS AFTER ADDITION

            curr = curr.next

            #move values of next place if it exists
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return Dummy.next
        