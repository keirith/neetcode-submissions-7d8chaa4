class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * (len(nums) * 2) #intialize enough space for ans array, fill with 0
        #n = len(nums) #capture length on nums array

        for i in range(len(nums)):
            ans[i] = nums[i]
            ans[i+len(nums)] = nums[i]
        return ans