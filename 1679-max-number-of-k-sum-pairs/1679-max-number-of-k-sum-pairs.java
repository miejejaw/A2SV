class Solution {
    public int maxOperations(int[] nums, int k) {
        Arrays.sort(nums);
        int count=0,left=0,right=nums.length-1;
        
        while(right>left){
            if(nums[left]+nums[right]>k)               
                right--;
            else if(nums[left]+nums[right]<k) 
                left++;
            else {
                count++;
                right--;
                left++;
            }
        }
        return count;
    }
}