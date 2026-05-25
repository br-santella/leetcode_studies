# Merge 2 string with max 100 letters

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

"""QUESTIONS
1. For what is used the self parameter in the function? Is necessary?
    Used for OOP. Self represents the specific object builted. It allows the functions inside the class to access or change that specific object's data.
2. Why to use a class Solution?
    To test your code, LeetCode has to run your function against hundreds of different test cases. By using a class, the platform can easily spin up a fresh, isolated instance of your code for every single test case, ensuring that leftover data from Test Case #1 doesn't accidentally mess up Test Case #2.
"""
