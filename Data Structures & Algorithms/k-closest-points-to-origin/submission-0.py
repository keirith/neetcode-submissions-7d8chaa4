import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''
        I want to use a heap to store a tuple leading with the euclid distances, then the cordinates of each point.
        I'll want to use a max heap to keep up to k cordinates, so the largest euclid distance gets evicted.
        '''
        my_heap = []

        for point in points:
            e_distance = abs(math.sqrt(((0 - point[0])**2 + (0 - point[1])**2)))
            heapq.heappush(my_heap, (-1 * e_distance, point))
            if len(my_heap) > k:
                heapq.heappop(my_heap)

        return [ h[1] for h in my_heap ]
        #Time: O(n log k)  n = len(points), k = restriction of number of points interested in.
        #space: O(k) , at most k elements placed on heap.
        