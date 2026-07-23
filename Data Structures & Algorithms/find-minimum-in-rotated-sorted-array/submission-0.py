class Solution:
    def findMin(self, nums: List[int]) -> int:
        #binary search
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2

            if nums[hi] > nums[mid]:
                hi = mid
            else: #nums[hi] < nums[mid]
                lo = mid + 1
        
        return nums[hi] #lo and hi should point to same after while loop
        #time: O(log n)
        #space: O(1)
