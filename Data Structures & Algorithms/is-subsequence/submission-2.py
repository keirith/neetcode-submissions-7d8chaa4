class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #can use two pointer method to progress through strings
        #if pointer reaches end of s -> return True
        #if pointer reaches end of t and s not at end -> return False
        #empty strings
        if len(s) == 0:
            return True

        i = 0
        for j in range(len(t)):
            if s[i] == t[j]:
                i += 1
            if i == len(s):
                return True
            
        return False
        
        
        