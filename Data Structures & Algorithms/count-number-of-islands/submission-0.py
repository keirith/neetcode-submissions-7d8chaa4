class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if self.dfs(grid, r, c, visited) == True:
                    count += 1
        return count


    def dfs(self, grid, r, c, visited):
        #define boundary for grid
        row_boundary = 0 <= r < len(grid)
        column_boundary = 0 <= c < len(grid[0])
        if not row_boundary or not column_boundary:
            return False
        #base conditions
        if grid[r][c] == "0": #water
            return False

        pos = (r,c)
        if pos in visited:
            return False
        
        visited.add(pos)

        #recursive case, explore land in 4 directions
        self.dfs(grid, r - 1, c, visited) #up
        self.dfs(grid, r + 1, c, visited) #down
        self.dfs(grid, r, c - 1, visited) #left
        self.dfs(grid, r, c + 1, visited) #right

        return True
        #Time: O(r*c) | Space: O(r*c)
