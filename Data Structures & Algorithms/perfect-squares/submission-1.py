import math
import sys

class Solution:
    def numSquares(self, n: int) -> int:
        sys.setrecursionlimit(20000)
        return self._numSquares(n, {})

    def _numSquares(self, n, memo):
        #base case - memoization
        if n in memo:
            return memo[n]
        #base case
        if n == 0:
            return 0

        min_squares = float("inf")
        #recursive step
        for i in range(math.floor(math.sqrt(n)), 0, -1):
            square = i * i #therefore when i = sqrt(n) => square = n, checking all perf squares <= n.
            num_squares = 1 + self._numSquares(n - square, memo) #DP recurrence: dp(n) = 1 + min(dp(n - s))
            min_squares = min(min_squares, num_squares)
            if min_squares <= 2: # optimization to reduce depth
                break

        memo[n] = min_squares
        return memo[n]

        #BF TC: O(sqrt(n)^n) => exponential
        #BF SC: O(n) - height of descision tree

        #with memoization TC: O(n*sqrt(n))