class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #search for the pivot point using binary search O(log n)
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < nums[hi]:
                #search left
                hi = mid
            elif nums[mid] > nums[hi]:
                #search right
                lo = mid + 1
        
        #loop concludes, both pointers pointing at pivot.
        #returning hi would result in the same. This should point to the smallest element pivot

        #at this point the array is split into two halves..
        #nums[0]...nums[pivot-1 (largest ele)] LEFT ARRAY
        #nums[pivot]...nums[len(nums)-1] RIGHT ARRAY
        # we need to search both halves (using bin search to find if target exists)

        def bin_search(lo, hi, target):
            while lo <= hi:
                mid = (lo + hi) // 2
                if nums[mid] < target:
                    lo = mid + 1
                elif nums[mid] > target:
                    hi = mid - 1
                else:
                    return mid #we found the target

            return -1 #target was not found
        
        larger_half = bin_search(0, lo-1, target)
        smaller_half = bin_search(lo, len(nums)-1, target)

        if larger_half != -1:
            return larger_half
        elif smaller_half != -1:
            return smaller_half
        else:
            return -1 #target not found in either half 
    

                

