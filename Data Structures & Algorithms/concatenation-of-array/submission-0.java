class Solution {
    public int[] getConcatenation(int[] nums) {
        int n = nums.length; //capture length of nums
        int[] ans = new int[2 * n]; //create new array of 2*n

        for(int i = 0; i < n; i++){
            ans[i] = nums[i]; //populates first half of ans
            ans[i + n] = nums[i]; //populates second half of ans
        }

        return ans;
    }
}