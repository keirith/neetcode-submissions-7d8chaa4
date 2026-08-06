class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self._wordBreak(s, wordDict, 0, {})

    def _wordBreak(self, s, wordDict, i, memo):
        #base case - from reference of index pos, finding case of empty string
        if i == len(s):
            return True

        #base case for memoization of changing atribute (i)
        if i in memo:
            return memo[i]

        #recursive step
        for word in wordDict:
            if s.startswith(word, i):
                if self._wordBreak(s, wordDict, i + len(word), memo) == True:
                    memo[i] = True
                    return memo[i]
        
        memo[i] = False
        return memo[i]
        