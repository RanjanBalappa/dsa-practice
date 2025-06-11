class Solution:
    def func(self, i1, j1, i2, j2, grid , dp):
        if j1 < 0 or j2 < 0 or j1 >= len(grid[0]) or j2 >= len(grid[0]):
            return -1e8
        
        if i1 == len(grid):
            return 0

        if dp[i1][j1][j2] != -1:
            return dp[i1][j1][j2]

        maxi = 0
        for d1 in range(-1, 2, 1):
            for d2 in range(-1, 2, 1):
                if i1 == i2 and j1 == j2:
                    score = grid[i1][j1] + self.func(i1 + 1,j1 + d1, i2 + 1, j2 + d2, grid, dp)
                else:
                    score = grid[i1][j1] + grid[i2][j2] + self.func(i1 + 1,j1 + d1, i2 + 1, j2 + d2, grid, dp)
                
                maxi = max(maxi, score)
                dp[i1][j1][j2] = maxi

        return dp[i1][j1][j2]
        
    def cherryPickup(self, grid: List[List[int]]) -> int:
        dp = [[[-1 for _ in range(len(grid[0]))] for _ in range(len(grid[0]))] for _ in range(len(grid))]
    
        return self.func(0, 0, 0, len(grid[0]) - 1, grid, dp)
        