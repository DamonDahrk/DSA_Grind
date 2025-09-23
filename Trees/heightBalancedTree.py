# Given a binary tree, return true if it is height-balanced and false otherwise.

# A height-balanced binary tree is defined as a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        #Here we have to do DFS again and then figure out the abs difference between left and right height
        #like that we can check if its true or false for the height balance from bottom up approach
        #by tracking height from leaves we can negate retraversal and hence make the sol O(n)

        def DFS(currLeaf):
            if not currLeaf:
                return [True,0] #zero height is always balanced
            
            left = DFS(currLeaf.left)
            right = DFS(currLeaf.right)

            is_height_balanced = right[0] and left[0] and (abs(left[1] - right[1]) <=1)

            return [is_height_balanced,1+max(left[1],right[1])]
        
        return DFS(root)[0] #this checks for all subtrees
         
        