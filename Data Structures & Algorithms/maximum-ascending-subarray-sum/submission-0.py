class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = nums[0]
        curr_sum = nums[0]
        for i in range(1,len(nums)):
            if nums[i] <= nums[i-1]:
                curr_sum = 0
            
            curr_sum += nums[i]
            res = max(res, curr_sum)

        return res

            
        