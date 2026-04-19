class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #INTUTION: iterate once through length of array and use hashmap to map 
        #element (key) to freq (value) Once in hashmap, fetch all values and then 
        #return kth largest keys.

        #concerns: the hashmap is not a sorted datastructure, would be compute expensive to fetch
        #all the values and deduce the highest kth values and their subsequent keys.

        freq_map = {}

        for num in nums:
                freq_map[num] = freq_map.get(num, 0) + 1 #set val to 0 if not in map, else add +1

        #The problem now is I should have a dict freq_map with element -> frequency, 
        #but I don't know how to sort said dict

        sorted_items = sorted(freq_map.items(), key=lambda x: x[1], reverse=True)

        top_k = sorted_items[:k]

        return [num for num, freq in top_k]