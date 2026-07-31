class Solution:
    def rob(self, nums: List[int]) -> int:
        return self._rob(nums, 0, {})

    def _rob(self, nums, i, memo):
        #base case for memo - adding each starting pos for shrinking array
        if i in memo:
            return memo[i]
        #base case - empty array
        if i >= len(nums):
            return 0

        #recursive step
        include = nums[i] + self._rob(nums, i + 2, memo) #can't consider neighbor
        exclude = self._rob(nums, i + 1, memo) #can consider neighbor, didn't rob at nums[0]
        memo[i] = max(include, exclude)
        return memo[i]

        #next optimize the slicing, as we run this for each recursive step, too expensive
        #use i to consider starting position on the reduced size array nums

        #implement memoization to speed up runtime of algorithm from exponential O(2^n) to linear O(n)
