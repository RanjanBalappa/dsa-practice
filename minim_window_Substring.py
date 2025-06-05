class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        m = len(t)
        hashmap = {}
        for i in range(m):
            hashmap[t[i]] = hashmap.get(t[i], 0) + 1

        l = 0
        r = 0
        count = 0
        minlen = float("inf")
        sidx = -1
        while r < n:
            hashmap[s[r]] = hashmap.get(s[r], 0) - 1
            if hashmap[s[r]] >= 0:
                count += 1
            
            while count == m:
                if minlen > r - l + 1:
                    minlen = r - l + 1
                    sidx = l
                hashmap[s[l]] = hashmap.get(s[l], 0) + 1
                if hashmap[s[l]] > 0:
                    count -= 1
                l += 1
            r += 1
        
        return "" if sidx == -1 else s[sidx:sidx+minlen]
            