class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #two pointers that slide towards eachother based on whether
        #>, < target.
        l = 0
        r = len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] > target:
                #too large, shift r inwards
                r -= 1
            elif numbers[l] + numbers[r] < target:
                #too small, shit l inwards
                l += 1
            else:
                return [l+1, r+1]
        
        return -1 #will not be executed, sol'n guarenteed

        #Time: O(n) - sliding pointers inwards, at most each element is scanned once. 
        #space: O(1) - pointer manipulation
        