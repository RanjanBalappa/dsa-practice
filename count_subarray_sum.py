from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = {}
        prefixsum = 0
        count = 0
        hashmap[0] = 1
        for i in range(len(nums)):
            prefixsum += nums[i]
            if prefixsum - k in hashmap:
                count += hashmap[prefixsum - k]
            
            hashmap[prefixsum] = hashmap.get(prefixsum, 0) + 1

        return count
        