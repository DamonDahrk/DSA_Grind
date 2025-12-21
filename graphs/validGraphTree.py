class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n :
            return True 
        #if no vertices exists then technically a tree exist so return True 

        hashMap = { i:[] for i in range(n) }

        for v1,v2 in edges:
            hashMap[v1].append(v2)
            hashMap[v2].append(v1)
        #add the vertices for undirected edges(either direction) so the neighbours be looking like this:
        # hashMap for every node to check for tree should look like:  
        # 0 <-> 1,4
        # 1 <-> 0,2,3

        visitSet = set() #again to check for any cycles detected
        
        #will check all nodes: 
        
        def dfs(i,prev): #we are adding previous value here to ignore false cycle as we are checking to other nodes incase
            if i in visitSet:
                return False
            #CYCLE DETECTED 

            visitSet.add(i)  #start processing and check for loop
            for j in hashMap[i]:
                if j == prev: #this completely accounts for false cycle as we move to next node 0 -> 1 0 was prev value so the 
                              #undirected directions to both 0 and other value from 1 branch wont return fake cycle 
                    continue   #exit the loop prematurely for such a case 
                if dfs(j,i) == False: #CYCLE detected here #also we checking all the below nodes and updating prevnode accordingly
                    return False 
                
            return True #after all that checks return True cuz this is a valid true
        
        #we still need to check for any rogue disconnected vertice which wont make a tree if it exists

        return dfs(0,-1) and len(visitSet) == n #if this and case is true only then return because it means all nodes have 
                                                #visited and there is no rogue nodes. start with -1 cuz its not possible from 0
        