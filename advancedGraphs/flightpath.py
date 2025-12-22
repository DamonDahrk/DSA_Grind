class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        hashMap = collections.defaultdict(list) #easy way to make the hashmap for the ticket nodes
        tickets.sort() #sorting the list before adding to hash
        for source,dest in tickets:
            hashMap[source].append(dest)
        #first drawing the graph connections in the HASHMAP
        Result = ["JFK"] #result list starts with JFK as per problem statement and also will have guaranteed one valid path  
        # JFK : [BUF]
        # BUF : [HOU]
        # HOU : [SEA]

        def dfs(node):
            if len(Result) == len(tickets) + 1 : #because we are popping the ticket first itself.
                return True
            if node not in hashMap:
                return False #because its not even connected to the graph so cant have a valid path 

            temp = hashMap[node] #the node where we are checking the paths from

            for i,v in enumerate (hashMap[node]):
                hashMap[node].pop(i)  #within the source node not the entire dictionary!!
                Result.append(v) #add a valid path for now
                if dfs(v):  #dfs starts where we check for this flight ticket path 
                    return True #correct path should return then 
                Result.pop() #path invalid remove from the answer
                hashMap[node].insert(i,v) #append adds at the end, insert adds at a specific index as mentioned here
            return False
        
        dfs("JFK") #start at jfk as stated in the pstatement
        return Result