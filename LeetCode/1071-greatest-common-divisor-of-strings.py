# Greatest Common Divisor of Strings [Easy][Acceptance: 53,8%]
# https://leetcode.com/problems/greatest-common-divisor-of-strings/description

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        #1. Combine both to check if GCD exists
        if str1 + str2 != str2 + str1:
            return ""

        #2. Verify if str2 is the GCD 
        elif str1.replace(str2, "") == "":
            return(str2)

        #3. Perform subtraction-based GCD logic using the lengths
        else:
            len1, len2 = len(str1), len(str2)
            while len1 != len2:
                if len1 < len2:
                    len2 = len2 - len1
                else:
                    len1 = len1 - len2

            return(str1[:len1])
        return


""" COMMENTS
- The greatest common divisor must be a prefix of each string
- If a GCD exists, the sum of both string in any order should be equal
- The verification of str2 asn the GCD is only to optimize memory use and runtime, not essential
- The core rule of the subtraction GCD method is this: If a smaller block can perfectly measure a larger block, 
it must also be able to perfectly measure the leftover piece when you cut the smaller block out of the larger one.
"""
