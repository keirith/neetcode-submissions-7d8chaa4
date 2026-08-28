class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #base case
        if len(nums) == 0:
            return [[]]

        #recursive step
        first = nums[0]
        subs_without_first = self.subsets(nums[1:])
        subs_with_first = []
        for sub in subs_without_first:
            subs_with_first.append([first, *sub])
        
        return subs_without_first + subs_with_first
        #TC: O(2^n)
        #SC: O(2^n)

'''
nums = [1,2,3]
[
[],[2],[3],[2,3] #subs_without_first
[1],[1,2],[1,3],[1,2,3] #subs_with_first
]
'''