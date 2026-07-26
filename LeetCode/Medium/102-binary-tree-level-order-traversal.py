# Binary Tree Level Order Traversal [Medium][Acceptance: 73.1%]
# https://leetcode.com/problems/binary-tree-level-order-traversal/description/

class Solution(object):
    def levelOrder(self, root):
        queue = deque([root])
        result = []

        while len(queue) > 0:
            level = []

            for i in range(len(queue)):
                node = queue.popleft()

                if node != None:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            
            if level != []:
                result.append(level)
            

        return result
