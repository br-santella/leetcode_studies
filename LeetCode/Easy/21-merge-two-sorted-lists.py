# Merge Two Sorted Lists [Easy][Acceptance: 68.6%]
# https://leetcode.com/problems/merge-two-sorted-lists/description/

class Solution(object):
    def mergeTwoLists(self, list1, list2):

        # Create a merge list
        start = ListNode(0)
        end = start

        # Find min(list1, list2) until one of them is empty        
        while list1 and list2: # List = [] -> None
            if list1.val <= list2.val:
                end.next = list1
                list1 = list1.next

            else:
                end.next = list2
                list2 = list2.next

            end = end.next
        
        if list1:end.next = list1
        if list2:end.next = list2

        return start.next
