import heapq

class KthLargest:

#making min heap so that we can remove any smaller elements out of k range, and anyway Kth largest element will be the smallest


    def __init__(self, k: int, nums: List[int]):
        self.minHeap,self.k = nums,k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)
        
        #constructor for heap

        

    def add(self, val: int) -> int:
        #what if elements are added in the stream:

        heapq.heappush(self.minHeap,val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap) #pop as long the length is bigger than K
        return  self.minHeap[0]  #ZEROTH value is always the min

        
