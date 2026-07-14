class Solution:
    def arrangeCoins(self, n: int) -> int:
        #the key here is to identify the math formula for how many
        #coins are required for each row.
        #n/2 * (n+1) = # of coins needed for n rows
        #^^ this is Gauss's formula for sumation of increasing list.
        #This effectively becomes our "guess" predicition
        lo = 1
        hi = n
        res = 0
        while lo <= hi:
            mid = (lo + hi) // 2 #mid is a check on number of rows
            coins = (mid/2) * (mid + 1)
            if coins > n:
                hi = mid - 1
            else:
                lo = mid + 1
                res = max(mid, res)
        
        return res


        