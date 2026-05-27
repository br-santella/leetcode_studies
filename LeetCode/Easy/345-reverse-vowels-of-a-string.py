# Reverse Vowels of a String [Easy][Acceptance: 61,3%]
# https://leetcode.com/problems/reverse-vowels-of-a-string/description

# LOGIC:
# 1. Pointer (i) runs through 0 -> len(s)-1, searching the first vowel
# 2. Pointer (j) runs through len(s)-1 -> 0, searching the last vowel
# 3. When both find a vowel they switch until i == j

class Solution:
    def reverseVowels(self, s: str) -> str:
        #Transform (s) into a list so we can swap letters
        word = list(s)

        #Use set to search through Hash Map: O(1) time complexity
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']) 

        i = 0
        j = len(word)-1

        while i < j:
            while i < j and word[i] not in vowels: 
                i += 1
            while i < j and word[j] not in vowels:
                j -= 1
            if i < j:
                word[i], word[j] = word[j], word[i]
                i += 1
                j -= 1
        return "".join(word)
                
                    
""" COMMENTS
-> When you should use a (set) to check if an element exists IN a collection:
    - You only care about checking membership (if item in collection).
    - You don't care about the order of the items.
    - You don't need to store duplicate items.
    - You are defining the collection statically (like vowels = {...}) or searching the same collection many times."""
