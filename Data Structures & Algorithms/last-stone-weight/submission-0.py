from heapq import *
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #convert stones into negative array, pre-req for using max_heap (pop largest elements)
        stones = [ -stone for stone in stones]

        #use heapify to make max_heap
        heapq.heapify(stones)

        #now we have a max_heap, lets simulate the game
        while len(stones) > 1:
            heaviest = abs(heapq.heappop(stones))
            second_heaviest = abs(heapq.heappop(stones))

            #do nothing if == since they are already popped, they destroy eachother

            if heaviest != second_heaviest:
                heapq.heappush(stones, -1*(heaviest - second_heaviest))
            
        if len(stones) == 1:
            return abs(stones[0])
        else:
            return 0
