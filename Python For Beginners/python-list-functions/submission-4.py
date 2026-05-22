from typing import List # this is used to add type hints for List type

def get_sum(nums: List[int]) -> int:
    #return sum(nums) - built in way using the sum() list method.
    total = 0
    for num in nums:
        total += num
    return total

def get_min(nums: List[int]) -> int:
    #return min(nums) - built in way using the min() list method.
    minimum = nums[0]
    for num in nums:
        if num < minimum:
            minimum = num

    return minimum

def get_max(nums: List[int]) -> int:
    #return max(nums) -direct way to find the max
    maximum = nums[0] #assign maximum to first element of list: nums
    for num in nums: #iterate over each num in nums
        if num > maximum: #check if num is > maximum
            maximum = num #if so, update maximum to that iteration of num
    return maximum #at the end of loop (once iterated through entire list) return the maximum.


    # for i in range(len(nums)): This index looping is not required bc we only care about
    #the values, not the positions of the loop for finding max,min,total.

    #     if nums[i] > maximum:
    #         maximum = nums[i]
    # return maximum

# do not modify below this line
print(get_sum([1, 2, 3, 4, 5]))
print(get_sum([5, 4, 5, 6]))

print(get_min([7, 3, 4, 5]))
print(get_min([5, 4, 5, 6]))

print(get_max([7, 3, 4, 5]))
print(get_max([5, 4, 5, 6]))
