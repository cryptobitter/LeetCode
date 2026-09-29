class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        if grid[0][0] == ')' or grid[m-1][n-1] == '(':
            return False
    
        dp = [set() for _ in range(n)]
        dp[0] = {1}
        
        for j in range(1, n):
            if 1 in dp[j-1]:
                b = 1 if grid[0][j] == '(' else -1
                if 1 + b >= 0:
                    dp[j].add(1 + b)
        
        for i in range(1, m):
            new_dp = [set() for _ in range(n)]
           
            for b in dp[0]:
                nb = b + (1 if grid[i][0] == '(' else -1)
                if nb >= 0:
                    new_dp[0].add(nb)
            for j in range(1, n):
                candidates = set()
                for b in new_dp[j-1] | dp[j]: 
                    pass
                for b in new_dp[j-1]:
                    candidates.add(b)
                for b in dp[j]:
                    candidates.add(b)
                delta = 1 if grid[i][j] == '(' else -1
                for b in candidates:
                    nb = b + delta
                    if nb >= 0:
                        new_dp[j].add(nb)
            dp = new_dp
        
        return 0 in dp[n-1]