class Solution {
    public int[] twoSum(int[] nums, int target) {
        //Brute Force method. use nested for loops that start at adjacent indexes, add each index value 
        //to see if them sum to target. If so return the index position of each. If not, continue iterating.

        for(int i = 0; i < nums.length ; i++){

            for(int j = i + 1; j < nums.length; j++){ //start at i+1 so i&j don't compare same indices
                if(nums[i] + nums[j] == target){
                    return new int[]{i, j};
                }

            }
        }
        return new int[]{}; //should not be executed, as solution is guarenteed by PS. 
    }
}