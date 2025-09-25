import heapq

# You are given an 2-D array points where points[i] = [xi, yi] represents the coordinates of a point on an X-Y axis plane. You are also given an integer k.

# Return the k closest points to the origin (0, 0).

# The distance between two points is defined as the Euclidean distance (sqrt((x1 - x2)^2 + (y1 - y2)^2)).

# You may return the answer in any order.

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        #we dont need to find the square root as we only need return the points not the distance

        minHeap = []
        for x,y in points:
            distance = x**2 + y**2 #since distance from origin 
            minHeap.append([distance,x,y]) #add the values to the minheap to be sorted later O1

        heapq.heapify(minHeap) #now its sorted to the min distance as the question wanted
        res = []

        while k>0: #return the k points
            distance, x , y = heapq.heappop(minHeap)
            res.append([x,y]) #only append the coordinates

            k -= 1

        return res #k points 
        