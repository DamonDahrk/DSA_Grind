class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set() #Here we will be adding the index position of valid any triplet so that we dont repeat matching chars on different index

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2] :
                continue 
            #the value in the particular triple is more than how can it even reach the target
            for i , number in enumerate (t): #particular triplet
                if target[i] == number: #if the number matches the exact value index of the target then add the index
                    good.add(i) #we can check for other index and values now
        
        return len(good) == 3 #true if it matched false if it ddint
        