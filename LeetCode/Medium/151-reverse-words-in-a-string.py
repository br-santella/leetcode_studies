# Reverse Words in a String [Medium][Acceptance: 56,5%]
# https://leetcode.com/problems/reverse-words-in-a-string/description

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])

"""How it works step-by-step:

    Step 1: s.split()
        This chops the string up wherever there is a space and turns it into a list of words.
        "Python is awesome" becomes ['Python', 'is', 'awesome']

    Step 2: [::-1]
        This is Python's slicing trick for reversing a list. It reads the list from right to left.
        ['Python', 'is', 'awesome'] becomes ['awesome', 'is', 'Python']

    Step 3: " ".join(...)
        This takes the reversed list and glues the words back together into a single string, putting a space between each one.
        ['awesome', 'is', 'Python'] becomes "awesome is Python"
"""
