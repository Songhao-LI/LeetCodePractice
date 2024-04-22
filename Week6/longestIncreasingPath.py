class Solution:

    def solve(self, i, j, matrix, m, n, dp):
        if dp[i][j]!=-1:
            return dp[i][j]
        ans = 0

        # up
        if (i-1>=0 and matrix[i][j]<matrix[i-1][j]):
            ans = max(ans, self.solve(i-1, j, matrix, m, n, dp))
        # right
        if(j+1<n and matrix[i][j]<matrix[i][j+1]):
            ans = max(ans, self.solve(i, j+1, matrix, m, n, dp))
        # down
        if(i+1<m and matrix[i][j]<matrix[i+1][j]):
            ans = max(ans, self.solve(i+1, j, matrix, m, n, dp))
        # left
        if(j-1>=0 and matrix[i][j]<matrix[i][j-1]):
            ans = max(ans, self.solve(i, j-1, matrix, m, n, dp))
        
        dp[i][j] = ans+1
        return dp[i][j]

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        ans = -1
        dp = [[-1]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                ans = max(ans, self.solve(i, j, matrix, m, n, dp))
        return ans