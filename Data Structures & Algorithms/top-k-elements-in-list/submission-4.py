import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #dict to track freq's of each num in nums
        #use a heap to ensure only top k freq elements remain and pop the result at end of nums.
        #heap sorts values based on FIRST VALUE of tuple provided.

        freq = {}
        my_heap = []

        for num in nums:
            freq[num] = 1 + freq.get(num, 0)

        #{1:3 , 2:2 , 3:1} num:frequency

        for num,frequency in freq.items():
            heapq.heappush(my_heap, (frequency, num))

            while len(my_heap) > k:
                heapq.heappop(my_heap)

        
        return [ num[1] for num in my_heap ]
        #TC: O(n log k)
        #SC: O(n + k) 

        