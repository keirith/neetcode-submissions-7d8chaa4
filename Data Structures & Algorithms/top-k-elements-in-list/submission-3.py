class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #count freq of nums using hash_map
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        my_heap = []
        for num in freq_map.keys():
            heapq.heappush(my_heap, (freq_map[num], num))

            if len(my_heap) > k:
                heapq.heappop(my_heap)
        
        return [ x[1] for x in my_heap ]
            
