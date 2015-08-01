"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

    11110
    11010
    11000
    00000
Answer: 1

    Example 2:

        11000
        11000
        00100
        00011
Answer: 3

Solution:
    A dfs approach, where any time we make a call to the inner dfs function
    from the outer function (not recursively), we increment the number of islands
"""

class Solution:
    # @param {character[][]} grid
    # @return {integer}
    def numIslands(self, grid):
        if not grid:
            return 0
        #grid = [list(row) for row in grid]
        nRows = len(grid)
        nCols = len(grid[0])
        visited = [[0]*nCols for i in range(nRows)]
        self.num_islands = 0
        
        def dfs(i,j):

            if i < 0 or i > nRows -1 or j < 0 or j > nCols - 1:
                return
            #print i,j, visited
            #pdb.set_trace() 
            if visited[i][j] == 1:
                return
            elif grid[i][j] == '1':
                visited[i][j] = 1
                dfs(i-1, j)
                dfs(i+1, j)
                dfs(i, j+1)
                dfs(i, j-1)
        for i in range(nRows):
            for j in range(nCols):
                if grid[i][j] == '1' and not visited[i][j]:
                    self.num_islands +=1
                dfs(i,j)
        return self.num_islands
    
if __name__ == "__main__":
    t0 = ['0'] #0
    t1 = ['11']#1
    t2 = ["111","000","111"] #2
    t3 = ["1011011"] #3
    S = Solution()
    print S.numIslands(t0) == 0
    print S.numIslands(t1) == 1
    print S.numIslands(t2) == 2
    print S.numIslands(t3) == 3
