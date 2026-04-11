class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        //create & initalize counter variables
        int current = 0;
        int max = 0;

        for(int i = 0; i < nums.length; i++){

            if(nums[i]==1){
                current++; //increment current counter
            }
            else{
                current = 0; //reset current counter
            }
            if(current > max){
                max = current; //update max to current if > existing max
            }
        }
        return max;
    }
}