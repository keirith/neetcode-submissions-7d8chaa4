class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current_ones = 0 #counter for current count of 1's
        max_ones = 0 #counter for max count of consecutives 1's
        for num in nums: #just need to consider value, not index
            if num == 1:
                current_ones += 1 #updates current
                if current_ones > max_ones: 
                    max_ones = current_ones #updates max_ones count if current count is larger
            else:
                current_ones = 0 #resets counter to zero
        return max_ones #returns answer

#O(n)Time n= length of the array | O(1)Space (simple reads of each array element once)

        