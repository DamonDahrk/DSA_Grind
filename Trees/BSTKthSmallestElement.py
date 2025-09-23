# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) in the tree.

# A binary search tree satisfies the following constraints:

# The left subtree of every node contains only nodes with keys less than the node's key.
# The right subtree of every node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees are also binary search trees.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0 #this is what we are gonna be testing our kth smallest integer against 
        stack = [] #stack to store and pop the leftest - cur - rightest values
                    #in order, since its bst we are in luck to always have sorted in order
        
        curr = root #tree node to be traversed:

        while curr or stack: #while stack is non empty or the curr has values in it
            while curr:
                stack.append(curr) #track all nodes as furthest left as possible
                curr = curr.left
            
            curr = stack.pop() #pop the current node and then inc the n count to get the kth smallest val
            n += 1
            if n == k:
                return curr.val  #if it matches to user input then return the value 
            curr = curr.right  #else go right of that particular leaf and continue  #popwise it will do it later

