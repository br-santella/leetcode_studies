# Validate Binary Search Tree [Medium][Acceptance: 36.1%]
# https://leetcode.com/problems/validate-binary-search-tree/description/

class Solution(object):
    def isValidBST(self, root):

        def validTree (node, min, max):
            if node == None:
                return True
            
            elif node.val <= min or node.val >= max:
                return False
            
            return (validTree(node.left, min, node.val) and validTree(node.right, node.val, max))

        return validTree(root, float("-inf"), float("inf"))
