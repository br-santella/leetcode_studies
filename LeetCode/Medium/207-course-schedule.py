# Course Schedule [Medium][Acceptance: 51.9%]
# https://leetcode.com/problems/course-schedule/description/

class Solution(object):
    def canFinish(self, numCourses, prereq):
        # Create a hashTable to map all courses prerequisites
        hashTable = {i: [] for i in range(numCourses)}
        for c, p in prereq: #Tuple unpacking
            hashTable[c].append(p)

        # Visites set for the path, not total search
        visited = set()
        def isValid(course):
            if course in visited: #In this path
                return False
            if hashTable[course] == []:
                return True

            visited.add(course)
            for pre in hashTable[course]: # Iterate list -> for x in list[]
                if not isValid(pre):
                    return False
            visited.remove(course)
            hashTable[course] = []
            return True

        for i in range(numCourses):
            if not isValid(i): return False # if not bool <-> if bool == False
        return True
