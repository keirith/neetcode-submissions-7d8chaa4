class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return self._uniquePaths(m,n,0,0,{})


    def _uniquePaths(self, m, n, r, c, memo):    
        #base cases
        #remembering (r,c) positions in memo
        if (r,c) in memo:
            return memo[(r,c)]
        #handle travel off grid
        if r == m or c == n:
            return 0
        #handle when we find bottom right corner
        if r == m - 1 and c == n - 1:
            return 1

        #recursive step
        move_down = self._uniquePaths(m,n,r+1,c, memo)
        move_right = self._uniquePaths(m,n,r,c+1, memo)
        memo[(r,c)] = move_down + move_right
        return memo[(r,c)]

    #next add memoization to DP sol'n
    #use top-down DP w/ memoization to solve this 2D DP problem