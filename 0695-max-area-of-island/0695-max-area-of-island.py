class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m=0 
        def fun(i,j):
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]==0:
                return 0
            grid[i][j]=0
            return 1+fun(i+1,j)+fun(i-1,j)+fun(i,j+1)+fun(i,j-1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    a=fun(i,j)
                    m=max(m,a)        
        return m