class Solution {
    public int minPairSum(int[] nums) {
        Arrays.sort(nums);
        int max=0;
        for(int i=0,j=nums.length-1; i<j; i++,j--){
            max= Math.max(max,nums[j]+nums[i]);
        }
        return max;
    }
}