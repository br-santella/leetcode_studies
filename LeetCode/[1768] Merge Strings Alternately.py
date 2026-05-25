# Merge 2 string with max 100 letters [Easy][Acceptance: 82,1%]
# https://leetcode.com/problems/merge-strings-alternately/description

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        while len(word1) > 0 and len(word2) > 0:
            result = result + word1[0] + word2[0]
            word1 = word1[1:]
            word2 = word2[1:]

        if len(word1) > 0:
            result = result + word1
        elif len(word2) > 0:
            result = result + word2

        return(result) 

sol = Solution() 
final_output = sol.mergeAlternately("abc", "pqr")
