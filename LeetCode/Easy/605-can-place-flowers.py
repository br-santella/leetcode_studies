# Can Place Flowers [Easy][Acceptance: 29,1%]
# https://leetcode.com/problems/can-place-flowers/description

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        freeSpots = 0

        for i in range(len(flowerbed)):
           if flowerbed[i]==0:
                prev = (i == 0 or flowerbed[i-1] ==0)
                next = (i == len(flowerbed)- 1 or flowerbed[i+1]==0)

                if prev and next:
                    flowerbed[i] = 1
                    freeSpots += 1
        
        return (freeSpots >= n)

"""COMMENTS
- This resolution focus on boolean (True/False) and operators logic to avoid IndexError finding prev and next values
- How Python treats or: When Python evaluates A or B, if A is True, Python doesn't even bother looking at B. 
  It already has what it needs for the whole statement to be True, so it stops evaluating right there.
"""
