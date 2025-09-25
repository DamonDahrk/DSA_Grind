# You are given an array of CPU tasks tasks, where tasks[i] is an uppercase english character from A to Z. You are also given an integer n.

# Each CPU cycle allows the completion of a single task, and tasks may be completed in any order.

# The only constraint is that identical tasks must be separated by at least n CPU cycles, to cooldown the CPU.

# Return the minimum number of CPU cycles required to complete all tasks.

# Example 1:

# Input: tasks = ["X","X","Y","Y"], n = 2

# Output: 5
from collections import Counter
import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        count = Counter(tasks) #we are calculating the max frequency of occurence of a letter here
                                #they will be creating a hash map anyways
        
        maxHeap = [-n for n in count.values()] #max heap creation on the frequencies
        heapq.heapify(maxHeap)
        q = deque()  #doubly linked list if we can pop from the left for that we added it (oldest val)
        time = 0
        while maxHeap or q:
            time += 1

            if maxHeap: #as long as the heap exists as we need to run all tasks to find time 
                DecrementedCharacterCount = 1 + heapq.heappop(maxHeap) #-ve characters for maxheap so we are adding 1 i.e reducing actually
                #inside the if
                if DecrementedCharacterCount: #if there is a count that was popped 
                    q.append([DecrementedCharacterCount,time+n]) #storing the decremented freq and the next time occurence
                                                           #it can be added to the heap again (n gap for indiv char)
            
            if q and q[0][1] == time: #if there is q and the time for freq is equal to when the character will be 
                                      #available again :
                    heapq.heappush(maxHeap, q.popleft()[0] ) #inserting only the decremented freq 

        return time #finally return the time it took to undergo the tasks


        