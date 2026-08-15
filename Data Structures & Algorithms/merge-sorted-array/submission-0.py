class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        
        fill through nums1 backwards. move pointers in reverse through both nums1 and nums2, taking the larger of two pointers to fill pointer k.
        initalize a pointer at end of nums1 (m+n-1) 
        initalize comparison pointers for nums 1 (m-1) and nums2 (n-1) 
        """
        if n == 0:
            return

        k = m + n - 1 #starts from end of zeros in nums1
        i = m - 1 #nums1 comparison pointer
        j = n - 1 #nums2 comparison pointer

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1