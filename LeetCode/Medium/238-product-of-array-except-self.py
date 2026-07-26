# Product of Array Except Self [Medium][Acceptance: 69.1%]
# https://leetcode.com/problems/product-of-array-except-self/description/

class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        pre, post = 1, 1
        result = [1] * n

        # Prefix 
        for i in range(n):
            result[i] = pre
            pre *= nums[i]

        # Postfix
        for i in range(n-1,-1,-1):
            result[i] *= post
            post *= nums[i]

        return (result)
