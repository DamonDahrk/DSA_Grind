# Maximum Depth of Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0   #return zero cuz no root exists

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        #again this is a depth first search where we go to bottom recursively and then count that node as height
        #take the max of left and right and use that to climb up to root and get the height by default.


        return (1+max(left,right))
        