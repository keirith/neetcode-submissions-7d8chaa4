class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #create a hashmap for nums1 and nums2, mapping element -> value (this doesnt matter)
        #fetch keys for both maps and compare. Return list of all shared keys

        nums1_hash, nums2_hash = {},{}

        for num in nums1:
            nums1_hash[num] = 0
        
        for num in nums2:
            nums2_hash[num] = 0

        common_keys = nums1_hash.keys() & nums2_hash.keys()
        return list(common_keys)