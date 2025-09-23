# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        #This is the same as previous problem of matching tree structure but for checking the subtrees
        #So we will use the soln of the previous problem as a helper function here

        def SameTree(p,q):
            if not p and not q :
                return True 
            
            if (not p and q) or (not q and p) :
                return False #not equal trees
            
            if p.val != q.val :
                return False # the values are not matching 
            
            return SameTree(p.left , q.left) and SameTree(p.right , q.right)
        
        def has_subtree(root):
            if not root:
                return False
            if SameTree(root, subRoot):
                return True  #if there is a subtree which is equal 
            return has_subtree(root.left) or has_subtree(root.right) #if not the main subtree maybe the left or right tree
                                                                    #has it


        return  has_subtree(root)

            
            
        