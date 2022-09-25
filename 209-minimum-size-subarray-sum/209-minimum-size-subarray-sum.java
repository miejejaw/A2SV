class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        for(int i=1; i<nums.length; i++){
            nums[i]+=nums[i-1];
        }
        int temp=0,min= Integer.MAX_VALUE;
        for(int i=0,j=-1; i<nums.length;){
            if(nums[i]-temp>=target){
                min = Math.min(min,i-j);
                temp=nums[++j];
            }
            else i++;
        }
        
        return (min!=Integer.MAX_VALUE)?min:0; 
    }
}