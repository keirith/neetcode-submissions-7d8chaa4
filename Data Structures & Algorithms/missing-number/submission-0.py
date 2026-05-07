class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        present = set(nums)

        for num in range(0, n + 1):
            if num not in present:
                return num
        
        return -1