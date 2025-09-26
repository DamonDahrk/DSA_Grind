# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        res = [] #result stored in a list string
        def dfs(node):
            if not node:
                res.append("N")  #null marker
                return 
            res.append(str(node.val)) #since it will be int so convert it to string first 
            dfs(node.left)  #left first
            dfs(node.right)   #right next
            

        dfs(root)
        return ",".join(res)  #get the string with commas 

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",") #get all vals now
        self.i = 0 #global variable to update in the recursion function below:
        
        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i])) #convert it back to int to store the values
                                               #after adding the value to tree then increment    
            self.i += 1           
            node.left = dfs()
            node.right = dfs()
            return node #return the node here 

        return dfs()

