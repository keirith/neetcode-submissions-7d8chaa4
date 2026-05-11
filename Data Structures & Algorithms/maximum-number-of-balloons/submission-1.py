class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        #create freq_map for characters (key) to occurences (val) in text
        freq_map = {}

        for c in text:
            freq_map[c] = freq_map.get(c, 0) + 1

        #we know the frequencies of char's in balloon. Can find the min
        #of each of these values

        return min(
            freq_map.get('b', 0),
            freq_map.get('a', 0),
            freq_map.get('l', 0) // 2, #two l's
            freq_map.get('o', 0) // 2, # two o's
            freq_map.get('n', 0),
        )

        #time complexity: O(n), looping string to create freq_map
        #space complexity: O(26) -> O(1) map contains at most 26 c's
        #representing lowercase alphabet
        