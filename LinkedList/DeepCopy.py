
# The deep copy should consist of exactly n new nodes, each including:

# The original value val of the copied node
# A next pointer to the new node corresponding to the next pointer of the original node
# A random pointer to the new node corresponding to the random pointer of the original node

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        copyNode = {None : None} #incase we run out of copy , this will have the copy

        curr = head #head as the current
        while curr:
            copy = Node(curr.val) #set only the value
            copyNode[curr] = copy #add it to our dictionary first
            curr = curr.next

        
        curr = head #head as the current #pass2
        while curr:
            copy = copyNode[curr]
            copy.next = copyNode[curr.next]
            copy.random = copyNode[curr.random]
            curr = curr.next
        
        return copyNode[head] #this is storing our copy linked list and will give that