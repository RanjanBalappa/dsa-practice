from typing import List

#https://leetcode.com/problems/two-sum/description/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            rem = target - num
            if rem in hashmap:
                return [hashmap[rem], i]
            hashmap[num] = i
