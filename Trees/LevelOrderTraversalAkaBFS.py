# Given a binary tree root, return the level order traversal of it as a nested list, where each sublist contains the values of nodes at a particular level in the tree, from left to right.

from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return [] #edgecase of returning []
        
        ans = [] #the list of lists that we will be returning
        queue = deque() #this is so we can pop from left stack to enable BFS
        queue.append(root) #append the base root atleast

        while queue: #while we have values in queue till we exhausted travelling all leaves
            levelwise = [] #this is where level wise result will be returned
            n = len(queue)
            for i in range(n):
                node = queue.popleft() #remove the oldest value i.e the leftest level order traversal
                levelwise.append(node.val) #add to level list the value of the popped node

                if node.left : queue.append(node.left)
                if node.right: queue.append(node.right) 

                #add to the queue  if there exist a left and right value in that order
            ans.append(levelwise) #add the levelwise result of a level to ans
        
        return ans 
                
            


        