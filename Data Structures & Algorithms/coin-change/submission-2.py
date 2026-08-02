class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        sys.setrecursionlimit(20000)
        ans = self._coinChange(coins, amount, {})
        if ans == float("inf"):
            return -1
        else:
            return ans

    def _coinChange(self, coins, amount, memo):
        #base case for what is changing to be memoized (amount)
        if amount in memo:
            return memo[amount]
        #base case, min ways to make an amount of 0.
        if amount == 0:
            return 0

        #base case, we have neg amount
        if amount < 0:
            return float("inf")


        #recursive step
        min_coins = float("inf")
        for coin in coins:
            res = self._coinChange(coins, amount - coin, memo)
            if res != float("inf"):
                num_coins = 1 + res
                if num_coins < min_coins:
                    min_coins = num_coins
        
        memo[amount] = min_coins
        return memo[amount]