import math 

class Solution:
    def check(self, piles, k, h):
        req_hours = 0
        for pile in piles:
            req_hours += math.ceil(pile/k)

        if req_hours <= h:
            return True
        return False


    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        while low <= high:
            mid = (low + high) // 2
            if self.check(piles, mid, h):
                high = mid - 1
            else:
                low = mid + 1

        return low

        
        