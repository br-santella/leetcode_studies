# Merge Intervals [Medium][Acceptance: 52.4%]
# https://leetcode.com/problems/merge-intervals/description/

class Solution(object):
    def merge(self, intervals):

        # Time-coplexity:
        # .sort() = O(nlogn)
        # For loop = O(n)
        # Total = O(nlogn) + O(n) = O(nlogn)
        
        new_min, new_max = 0, 0

        if not intervals:
            return []

        time = sorted(intervals)
        new_time=[]

        for x in range(len(time)):
            # Start new_min and new_max values
            if x == 0:
                new_min = time[x][0]
                new_max = time[x][1]

            # Identify if next item should be merged
            if time[x][0] <= new_max and time[x][1] > new_max: 
                new_max = time[x][1]

            # Identify if we add and start new count
            if time[x][0] > new_max:
                new_time.append([new_min, new_max])
                new_min = time[x][0] 
                new_max = time[x][1]

            # Treat last element
            if x == len(time)-1:
                new_time.append([new_min, new_max])          

        return new_time
