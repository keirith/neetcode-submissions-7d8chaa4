from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            ch_count = [0] * 26
            for ch in word:
                ch_count[ord(ch) - ord('a')] += 1
            
            key = tuple(ch_count)
            anagrams[key].append(word)

        return list(anagrams.values())