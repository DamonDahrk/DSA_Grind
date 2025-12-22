class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        #we need greedy approach we need the min number at first to form the consecutive group of straights so we use minheap

        if len(hand) % groupSize != 0:
            return False 
        
        #it has to be divisible to make the groups in the first place else forget about it .

        counter = {} #first we make a counter for hashmap 
        for n in hand:
            counter[n] = 1 + counter.get(n,0) #this tries to find the key for value else return 0 if it doesnt exist

        #dict function works like, n is 2 in list, if there is a prior occurence count.get(2) -> finds say 2 count already then add 1
        # if it doesnt exist then return 0

        minHeapValues = list(counter.keys()) #this will give the value list of the individual hand and not the count 
        heapq.heapify(minHeapValues) #this creates the minheap. and sorts it as well

        #minheap: [1,2,3,3,4,5,6,7] , counter will have the count

        while minHeapValues:
            first = minHeapValues[0] #smallest value:
            for hand in range (first,first+groupSize): #will continue from min value always to make the groups
                if hand not in minHeapValues:
                    return False
                #if the value only is not there how can we even make the consecutive groups
                counter[hand] -= 1 #reduce the count by one 
                if counter[hand] == 0:
                    if hand != minHeapValues[0]: #if the to be popped value is not the minimum
                        return False
                    heapq.heappop(minHeapValues) #let go cuz count has reached zero loop starts again from start to check for min most in the card list

        return True #it passes all checks mentioned above so it counts
                    

        