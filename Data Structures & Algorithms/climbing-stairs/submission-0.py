class Solution:
    def climbStairs(self, n) -> int:
        return self._climbStairs(n, {})


    def _climbStairs(self, n, memo):
        #base case
        if n in memo:
            return memo[n]
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        #recursive step
        memo[n] = self._climbStairs(n-1, memo) + self._climbStairs(n-2, memo)
        return memo[n]



        