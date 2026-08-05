class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self._longestCommonSubsequence(text1, text2, 0, 0, {})

    def _longestCommonSubsequence(self, text1, text2, i, j, memo):
        #base case, handling an empty string from index
        if i == len(text1) or j == len(text2):
            return 0

        #base case, handling memoization of changing atributes i & j
        if (i,j) in memo:
            return memo[(i,j)]


        #recursive step (2 steps, if matching... else not)
        if text1[i] == text2[j]:
            memo[(i,j)] = 1 + self._longestCommonSubsequence(text1, text2, i+1, j+1, memo)
            return memo[(i,j)]
        else:
            memo[(i,j)] = max (
                self._longestCommonSubsequence(text1, text2, i+1, j, memo),
                self._longestCommonSubsequence(text1, text2, i, j+1, memo)
            )
            return memo[(i,j)]
        
        #brute force recursion works, now optimize with memoization.