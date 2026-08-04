from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = Counter(s)
        count = 0
        at_least_one_odd_val = False

        #use a Counter to get counts of each ch in s (upper and lower).
        #iterate through freq's of each letter. freq/2 = count
        #need to handle case where odd number of freq, as 1 odd letter is permitted

        for val in freq.values():
            if val % 2 == 0: # if there is an even number of occurrences
                count += (val // 2)

            elif val % 2 != 0: #odd
                count += (val // 2)
                at_least_one_odd_val = True

        return count * 2 if not at_least_one_odd_val else (count * 2) + 1
            