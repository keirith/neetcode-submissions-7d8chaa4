from collections import deque
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #implement merge sort
        #base case - sort an array of size 1
        if len(nums) <= 1:
            return nums

        #recursive step
        mid = len(nums) // 2
        left_sorted = self.sortArray(nums[:mid])
        right_sorted = self.sortArray(nums[mid:])
        return self.merge(left_sorted, right_sorted)

    def merge(self, list1, list2):
        res = []
        list1 = deque(list1)
        list2 = deque(list2)
        while list1 and list2:
            if list1[0] < list2[0]:
                res.append(list1.popleft())
            else:
                res.append(list2.popleft())
        
        res += list1
        res += list2
        
        return res