class Solution {
    public int[] rearrangeArray(int[] nums) {
        Arrays.sort(nums);
        for(int i=0,k=1; k<nums.length; i+=2,k+=2){
            int temp=nums[i];
            nums[i]=nums[k];
            nums[k]=temp;
        }
        return nums;
        
    }
}