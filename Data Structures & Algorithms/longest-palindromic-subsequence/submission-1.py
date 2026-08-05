class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        return self._longestPalindromeSubseq(s, 0, len(s)-1, {})

    def _longestPalindromeSubseq(self, s, i, j, memo):
        #base case - looking at single letter array
        if i == j:
            return 1
        
        #base case - looking at size zero array
        if i > j:
            return 0

        #base case - memoizing changing index positions
        if (i,j) in memo:
            return memo[(i,j)]

        
        #recursive step
        if s[i] == s[j]:
            memo[(i,j)] = 2 + self._longestPalindromeSubseq(s, i + 1, j - 1, memo)
            return memo[(i,j)]

        else:
            memo[(i,j)] = max(
                self._longestPalindromeSubseq(s, i + 1, j, memo), 
                self._longestPalindromeSubseq(s, i, j - 1, memo)
            )
            return memo[(i,j)]


        