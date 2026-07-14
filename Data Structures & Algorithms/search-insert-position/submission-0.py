class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
# [-1 0 2 4 6 8].  t=5
#  l    m     h
#         l m h
#         lh
#         h l.    lo points to where element should be placed.

        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if target < nums[mid]:
                hi = mid - 1
            elif target > nums[mid]:
                lo = mid + 1
            else:
                return mid
        
        return lo #once pointers cross, lo will point where element should be place
        #time: O(log n)
        #space: O(1)
                