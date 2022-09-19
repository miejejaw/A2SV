class Solution {
    public int maxFrequency(int[] nums, int k) {
        
        Arrays.sort(nums);
        int l=nums.length-1,r=nums.length-2,max=1;
        while(r>=0){           
            if(nums[r]+k>=nums[l]){                
                k-=nums[l]-nums[r];
                r--; 
                max=Math.max(max,l-r);
            }
            else{
                l--;
                k+=(l-r)*(nums[l+1]-nums[l]);
            }            
        }
        return max;
    }
}