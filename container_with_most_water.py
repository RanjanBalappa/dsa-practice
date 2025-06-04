#https://leetcode.com/problems/container-with-most-water/description/

from typing import List 
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n - 1
        maxarea = 0
        while l < r:
            min_height = min(height[l], height[r]) 
            maxarea = max(maxarea, (r - l) * min_height)
            if height[l] < height[r]:
                l = l + 1
            else:
                r = r - 1

        return maxarea


        