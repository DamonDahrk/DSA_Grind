# You are given the root of a binary tree. Return only the values of the nodes that are visible 
# from the right side of the tree, ordered from top to bottom.


from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return [] #edge case for the fact that there might not be any value in tree

        queue = deque()
        queue.append(root)
        #again for popleft and BFS deque is required
        ans = [] #where will be sending right values only

        while queue:
            #while queue exists excecute the following:
            n = len(queue)
            rightSide = 0
            for i in range(n):
                node = queue.popleft()
                if node:
                    rightSide = node #keep storing the value of oldest popped as once the loop ends we will be left
                                     #with the rightmost value only , for the particular level
                    queue.append(node.left)
                    queue.append(node.right)
            if rightSide: #if there exists this value then add to the answer list
                ans.append(rightSide.val)
        return ans
        
        