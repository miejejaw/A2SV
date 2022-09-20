class Solution {
    public int maxOperations(int[] nums, int k) {
        Arrays.sort(nums);
        int count=0,l=0,r=nums.length-1;
        while(r>l){
            if(k-nums[l]==nums[r]){
                count++;
                l++;
                r--;
            }
            else if(k-nums[l]>nums[r]) l++;
            else r--;
        }
        return count++;
    }
}