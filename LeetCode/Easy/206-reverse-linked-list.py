# Reverse Linked List [Easy][Acceptance: 80.8%]
# https://leetcode.com/problems/reverse-linked-list/description/

class Solution(object):
    def reverseList(self, head):
        # Linkedlist -> Array
        array=[]
        while head:
            array.append(head.val)
            head = head.next


        # Array -> Linkedlist
        array.reverse()
        head = ListNode(0)
        start = head
        
        for i in array:
            head.next = ListNode(i)
            head = head.next
        
        return start.next
