class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #1 create freq map and organize nums by num -> freq
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num,0)+1

        #2 create buckets for organizing data from freq to value
        buckets = [[] for _ in range(len(nums)+ 1)]
        for num, freq in freq_map.items():
            buckets[freq].append(num)
        
        #3 collect top k buckets
        result = []
        for i in range(len(buckets)-1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result