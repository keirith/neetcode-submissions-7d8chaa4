#build decision tree by coin level to ensure no repeat combinations. 
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        return self._change(amount, coins, 0, {})
    
    def _change(self, amount, coins, i, memo):
        #base case, memoize what is changing.
        if (amount, i) in memo:
            return memo[(amount, i)]
        #base case, amount is zero
        if amount == 0: #question im asking.. how many ways can I make 0 amount? ans: 1 way with 0 coins.
            return 1
        #base case for coins array.. making sure we just iterate through coins we have.
        if i == len(coins):
            return 0
        
        coin = coins[i] #selecting a coin from coins to reduce amount
        total_ways = 0
        for qty in range(0, (amount // coin) + 1):
            remainder = amount - (qty * coin)
            total_ways += self._change(remainder, coins, i + 1, memo)
        
        memo[(amount, i)] = total_ways
        return memo[(amount, i)]
        
        #memoize
        #Time: O(a * c) amount * # of coins
        #space: O(a * c)