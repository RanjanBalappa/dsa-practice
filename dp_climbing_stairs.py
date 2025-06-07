class Solution:
    def ways(self, n, memo):
        
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        if memo[n] != -1:
            return memo[n]
        
        memo[n-1] = self.ways(n - 1, memo)
        memo[n-2] = self.ways(n - 2, memo)
        return memo[n-1] + memo[n-2]

        
    def climbStairs(self, n: int) -> int:
        memo = [-1] * (n + 1)
        return self.ways(n, memo)

        