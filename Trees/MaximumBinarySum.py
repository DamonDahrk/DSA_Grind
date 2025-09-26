# Given the root of a non-empty binary tree, return the maximum path sum of any non-empty path.

# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes has an edge connecting them. A node can not appear in the sequence more than once. The path does not necessarily need to include the root.

# The path sum of a path is the sum of the node's values in the path.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #we will be using a list value here so we can update it in recursion otherwise it causes 
        #confusion between global value and local value

        res = [root.val] 

        def dfs(root):
            if not root:
                return 0 #no root exists 
            
            leftMax = (dfs(root.left))
            rightMax = (dfs(root.right))
            leftMax = max(leftMax,0) #this makes sure that the value is positive and not integer
                                      #if it is negative dont bother taking that path at all for max sum 
            rightMax = max(rightMax,0)

            #if splitting:

            res[0] = max(res[0], leftMax + rightMax + root.val)
            #from bottom before we backtrack we are calculating the splits and updating the result accordingly

            return root.val + max(leftMax,rightMax) #once we are going up we cannot used the split paths the below ones had
            #so we are returning non split paths for upstairs 
            #since res has the max path it will only give the max sum paht back

        dfs(root) #start at the top
        return res[0] #return value within the list
        