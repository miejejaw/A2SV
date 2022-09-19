class Solution {
    public int maxFrequency(int[] nums, int k) {
        Arrays.sort(nums);
        int max=0,sum=0;
        for(int i=0,j=0; i<nums.length; i++){
            sum+=nums[i];
            if((i-j+1)*nums[i]-sum <= k)
                max=Math.max(max,i-j+1);
            else
                sum-=nums[j++];         
        }
        return max;
    }
}