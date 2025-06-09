class Solution:
    def count_func(self, dp, m, n):
        #base condition
        if m == 0 or n == 0:
            return 1
        if dp[m][n] != -1:
            return dp[m][n]
        left = self.count_func(dp, m-1, n)
        top = self.count_func(dp, m, n-1)
        dp[m][n] = left + top
        return dp[m][n]
        

    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)] 
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
            
        return dp[m-1][n-1]
        