class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #naive solution, sort the array and use conditionals
        #to check if n+1 is after n... O(nlog n) TC.. can do better 
        
        '''
        convert nums to a set. Check if each element is the start of a 
        sequence.. ie does set(n-1) exist. 
        '''
        set_nums = set(nums)
        longest = 0

        for num in nums:
            if (num - 1) not in set_nums:
                length = 0
                while (num + length) in set_nums:
                    length += 1
                longest = max(longest, length)
        
        return longest
        #time: O(n)
        #space: O(n)

