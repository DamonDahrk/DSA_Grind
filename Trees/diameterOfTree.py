# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        #kinda nuanced

        if not root:
            return 0
        
        self.diameter = 0 # creating a global variable to be used to calculate the longest path and return the result

        def DFSdiameter(curr):

            if not curr:
                return 0

            left = DFSdiameter(curr.left) #go to bottom
            right = DFSdiameter(curr.right) 

            self.diameter = max(self.diameter,(left+right)) #only get the max value
            return 1 + max(left, right) #has to return the height 
        
        DFSdiameter(root) #start at the root and then go to the children leaves
        return self.diameter
        



        