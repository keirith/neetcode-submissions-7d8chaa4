class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc_l = 1
        dec_l = 1
        max_l = 1
        for i in range(len(nums)-1):
            if nums[i + 1] > nums[i]:
                inc_l += 1
                dec_l = 1

            elif nums[i + 1] < nums[i]:
                inc_l = 1
                dec_l += 1
            
            else:
                inc_l = 1
                dec_l = 1
        
            max_l = max(max_l, inc_l, dec_l)

        return max_l
            


            
        