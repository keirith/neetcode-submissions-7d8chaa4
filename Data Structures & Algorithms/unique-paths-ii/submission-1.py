class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        return self.helper(obstacleGrid, 0, 0, {})

    def helper(self, obstacleGrid, r, c, memo):
        #base cases
        #adding known paths to memo
        if (r,c) in memo:
            return memo[(r,c)]
        #traversing off grid or into a wall
        if r == len(obstacleGrid) or c == len(obstacleGrid[0]) or obstacleGrid[r][c] == 1:
            return 0
        
        #finding the bottom right corner.
        if r == len(obstacleGrid) - 1 and c == len(obstacleGrid[0]) - 1:
            return 1

        #recursive step
        move_down = self.helper(obstacleGrid, r + 1, c, memo)
        move_right = self.helper(obstacleGrid, r, c + 1, memo)
        memo[(r,c)] = move_down + move_right
        return memo[(r,c)]

        #implement memoization to the base case.
        