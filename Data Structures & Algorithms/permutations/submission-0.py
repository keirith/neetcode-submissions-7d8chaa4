class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #base case
        if len(nums) == 0:
            return [[]]

        #recursive step
        first = nums[0]
        full_permutations = []
        for perm in self.permute(nums[1:]):
            for i in range(len(perm) + 1):
                full_permutations.append(perm[:i] + [first] + perm[i:])

        return full_permutations
        #TC && SC: O(n!)

'''
Input: nums = [2,3]
first = 1
perm = [2,3]

Output: [[1,2,3], [2,1,3], [2,3,1]
[1,3,2], [3,1,2], [3,2,1]]
'''
        