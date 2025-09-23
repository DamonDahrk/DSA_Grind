# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def checkTreeLeaf(p,q):
            if not p and not q:
                return True #structure is the same for no values
            
            if (not p and q) or (not q and p):
                return False #if one exists and the other doesnt there is a structure issue

            if (p.val != q.val) or (q.val != p.val) :
                return False #the values are not matching for the leaves 

            return checkTreeLeaf(p.left,q.left) and checkTreeLeaf(p.right,q.right)
            #check both leaves till you get to end

        return checkTreeLeaf(p,q)
        