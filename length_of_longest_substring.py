#https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        l = 0
        r = 0
        hashmap = {}
        longest = 0
        while r < len(s):
            while s[r] in hashmap and l <= hashmap[s[r]]:
                l = l + 1 
            
            hashmap[s[r]] = r
            longest = max(longest, r - l + 1)
            r = r + 1

        return longest

        