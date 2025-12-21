class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courseHashMap = { i:[] for i in range (numCourses) }
        #making the dictionary hash map 

        for course,prereq in prerequisites:
            courseHashMap[course].append(prereq) #adding the prereq
        
        #making the hash map as previous problem 
        output = [] #it will initialized empty where we add the optimal pathing
        visitSet , cycleSet  = set() , set()
        #check for cycles in the prereq course graph pathing
        def dfs(course):
            if course in cycleSet:
                return False  #cycle DETECTED!!
            if course in visitSet:
                return True #already been visited and cycle proof so safe
            
            cycleSet.add(course)
            for prereq in courseHashMap[course]:
                if dfs(prereq) == False : # CYCLE DETECTED!! THEN RETURN FALSE immediately 
                    return False 
            cycleSet.remove(course) #cycle is not there, hence safe !!
            visitSet.add(course)
            output.append(course) #now add this to the output order list as we established its safe
            return True 
        
        for course in range(numCourses):
            if dfs(course) == False : # CYCLE DETECTED!! THEN RETURN empty list immediately 
                    return [] 
        
        return output

