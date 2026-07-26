# 3Sum [Medium][Acceptance: 39.5%]
# https://leetcode.com/problems/3sum/description/

class Solution(object):
    def threeSum(self, nums):

        n = len(nums) 
        nums.sort()
        result= set()

        for i, x in enumerate(nums):
            # Avoid reuse the same values
            if i > 0 and x == nums[i-1]:
                continue

            hash = {}
            target = 0 - x

            for j, y in enumerate(nums):
                if i == j:
                    continue

                z = target - nums[j]

                if (z) in hash and ((x+y+z) == 0):
                    result.add(tuple(sorted((x,y,z))))

                hash[nums[j]] = 1

        return list(result)
