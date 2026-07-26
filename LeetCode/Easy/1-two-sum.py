# Two Sum [Easy][Acceptance: 57.9%]
# https://leetcode.com/problems/two-sum/description/

class Solution(object):
    def twoSum(self, nums, target):

        # Previous number mapping,
        hash = {} 

        for i, n in enumerate(nums): 
                    # ^ enumerate: catch value and infex at the same time

            diff = target - n

            # Check for existance
            if diff in hash: 
                return[hash[diff], i]

            hash[n] = i
        return
