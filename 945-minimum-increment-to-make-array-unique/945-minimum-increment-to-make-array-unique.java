class Solution {
    public int minIncrementForUnique(int[] nums) {

        Arrays.sort(nums);
        int count=0,val=nums[0];
        for(int i=1;i<nums.length; i++){            
            if(nums[i]>val) val=nums[i];
            else {
                 val++;              
                 count+=val-nums[i];                 
            }            
        }
        return count;
    }
}