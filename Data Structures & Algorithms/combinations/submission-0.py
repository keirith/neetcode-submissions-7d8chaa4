class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        #base case for k
        if k == 0:
            return [[]]
        
        #base case for n:
        if n < k:
            return []

        #recursive step (for including first number)
        first = n

        combos_with_first = []
        partial_combos = self.combine(n - 1, k - 1)
        for partial_combo in partial_combos:
            combos_with_first.append([first, *partial_combo])
        
        #recursive (for excluding first number)
        combos_without_first = self.combine(n - 1, k)

        return combos_with_first + combos_without_first
        #O(k choose n)