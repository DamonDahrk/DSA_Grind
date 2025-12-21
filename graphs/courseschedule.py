class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        courseHashMap = { i:[] for i in range (numCourses)  } #hash map list creation

        for prereq,course in prerequisites:
            courseHashMap[course].append(prereq) #to dictionary you have to append 

        visitSet = set() #here we can check if a cycle exists or not in case

        #We will be creating a hash map to track the prequisite courses of a course and check them out if its correct or not on completion

        # course : prereq
        #   0    : 1,2
        #   1    :  2
        #   2    :  [] 

        def dfs(course):
            if course in visitSet: #The cycle is confirmed here 
                return False
            if courseHashMap[course] == []:  #this is to prevent repeated computations as well 
                return True   #The prereq has already matched for this course so it can be true

            # --- BASE CHECKS ENDS -------
            
            visitSet.add(course) # add the course for cycle checking from here 
            for prereq in courseHashMap[course]:   #CHECKING FOR EVERY PREREQ thats why we need the below : 
                if not dfs(prereq):  #CYCLE DETECTS FALSE , FALSE FALSE IS TRUE AND THEN WE RETURN FALSE FOR THIS CYCLE
                    return False
            visitSet.remove(course)   #cycle doesnt exist is confirmed and we can remove it from the set 
            courseHashMap[course] = []   # all the prereq has been crossed out so remove them here and go to earlier branches
            return True                  # this course has been traversed and completed so mark it as true
        
        for course in range (numCourses):  # WE HAVE TO CHECK for EVERY COURSE THE VALIDITY #what if its not connected 
            if not dfs(course):
                return False
        return True   #then return True if its valid 
