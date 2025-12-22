class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #Dijkstra's Algo which uses bread first search:  #  Shortest distance

        EdgeDirection = collections.defaultdict(list) #make a dict of list where we can add the nodes and their respective neighbour and weight

        for (u,v,w) in times:
            EdgeDirection[u].append((v,w))  #adding the neighbour and weight to dictionary
        
        # 1 - 2,1 | 2 - 3,1 | 1 - 4,4  | etc....

        visit = set() # to keep track of nodes visisted from signal node.

        t = 0 # time taken to reach all nodes from signal

        minHeap = [(0,k)] # the node is going to be signal node to start off, 0 will be the weight (of itself)
        
        ## BFS Start ##

        while minHeap: #as long as minHeap is not empty
            w1,n1 = heapq.heappop(minHeap) #only min weight from signal node will be sent out (kinda base condition)
            if n1 in visit:
                continue # ignore the loop since we already visited this node from the singal node
            visit.add(n1) #visiting so lets add this node (from this node to other nodes)

            t = max(t,w1) #djikstra algo main max shortest distance, so t will always keep increasing as there is no way it will decrease.

            for n2,w2 in EdgeDirection[n1]:
                if n2 not in visit:  #the signal node connected to multiple nodes so this is BFS here adding 
                    heapq.heappush(minHeap,(w2+w1,n2)) #since we are calcing time we are adding the weights to find the signal sent to a node
        
        return t if n == len(visit) else -1 #ensure there are no rogue nodes visiting all nodes implies all are covered




