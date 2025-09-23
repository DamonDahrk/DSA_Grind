# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #We need to follow the logic of left < value < right , this has to hold true to accurate make a BST
        #Keep in mind it has to be consistent to the root value
        def isvalid(node, left, right):

            if not node:
                return True
            
            #no bst technically means it is correct as there is nothing to check against

            if not (node.val>left and node.val<right):
                return False
            #it has to follow that logic to keep the small values on left and greater values to right

            return (isvalid(node.left,left,node.val) and isvalid(node.right,node.val,right)) #val has to be less than
                                                                                            # right and val to be greater
                                                                                            #than left


    
        return isvalid(root, float('-inf'), float('inf')) #starter values
            
        