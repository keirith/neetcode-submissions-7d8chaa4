class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #create a hashmap to store value and its key(index)
        lookup = {} #dictionary: value -> index

        #use for loop to iterate i over range len(nums), check each value if it
        #exists in map, if not add to map. Then check if nums[i] - target = value
        for i, num in enumerate(nums):
            diff = target - num

            if diff in lookup:
                return [lookup[diff], i]
            
            lookup[nums[i]] = i
