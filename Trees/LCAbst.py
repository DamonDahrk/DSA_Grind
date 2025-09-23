# Given a binary search tree (BST) where all node values are unique, and two nodes from the tree p and q, return the lowest common ancestor (LCA) of the two nodes.

# The lowest common ancestor between two nodes p and q is the lowest node in a tree T such that both p and q as descendants. The ancestor is allowed to be a descendant of itself.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root # we are starting at the root

        while curr:
            #loop will run as long as we iterate to find the lowest common ancestor through all leaves
        
            if (p.val < curr.val) and (q.val < curr.val): #its a BST so we will go to lowest option or go to nearest pq
                curr = curr.left 
            elif(p.val > curr.val) and (q.val > curr.val):
                curr = curr.right
            else:
                return curr  #in case of uneven match the root has to be the LCA even if itself 
        return root #if no LCA then return itself
        