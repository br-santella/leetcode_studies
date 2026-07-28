# Valid Parentheses [Easy][Acceptance: 44.6%]
# https://leetcode.com/problems/valid-parentheses/description/

class Solution(object):
    def isValid(self, s):
        par = {'(' : ')', '[' : ']', '{' : '}'}
        stack = [] 

        for i in s:
            if i in par: 
                stack.append(par[i])
            if i not in par:
                if len(stack) == 0:
                    return False
                if (len(stack) > 0 and stack.pop() != i):
                    return False

        return not len(stack) > 0
