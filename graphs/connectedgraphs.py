class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #very easy,

        hashMap = { i: [] for i in range (n)}  #create hashmap for the vertices and their connections

        for v1,v2 in edges:  #undirected again
            hashMap[v1].append(v2)
            hashMap[v2].append(v1)
        
        visit = [False] * n #Initially set as false list so we can seperated the connected vertices from disconnected ones 

        def dfs(node):
            for neighbourNode in hashMap[node]:
                if not visit[neighbourNode]:
                    visit[neighbourNode] = True
                    dfs(neighbourNode)
        
        #this makes sure the connected ones are seperate from the already connected ones and takes them as one whole part
        
        totalConnectedGraphs = 0
        for node in range(n):
            if not visit[node]:
                visit[node] = True
                dfs(node)
                totalConnectedGraphs += 1
        
        return totalConnectedGraphs
        
        