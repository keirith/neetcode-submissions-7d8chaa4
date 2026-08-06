from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = {}
        for c in magazine:
            d[c] = d.get(c, 0) + 1
        
        for c in ransomNote:
            d[c] = d.get(c, 0) - 1
            if d[c] < 0:
                return False

        return True
        

        