# Longest Substring Without Repeating Characters [Medium][Acceptance: 39.6%]
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution(object):
    def lengthOfLongestSubstring(self, s):
 
        # "Sliding window" algorithm
        window = set()
        start = 0
        maxSize = 0

        for i in range(len(s)):

            while s[i] in window:
                window.remove(s[start])
                start += 1
            window.add(s[i])
            maxSize = max(maxSize, i-start+1)

        return maxSize
