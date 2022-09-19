class Solution {
    public int maxFrequency(int[] nums, int k) {
        Arrays.sort(nums);
        int max=1,count=1,i=nums.length-2,j=nums.length-1;
        while(i>=0){
            if(k>=nums[j]-nums[i]){
                k-=nums[j]-nums[i];
                i--;
                count++;
                max=Math.max(count,max);
            }
            else{
                j--;
                count--;
                k+=(nums[j+1]-nums[j])*(j-i);
            }
        }
        return max;
    }
}